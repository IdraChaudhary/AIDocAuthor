from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.services.llm_adapter import MockLLM
router = APIRouter()

llm = MockLLM()

@router.post('/project/{project_id}/section/{section_id}')
def generate_section(project_id:int, section_id:int, db: Session = Depends(get_db)):
    s = db.query(models.Section).filter(models.Section.id==section_id, models.Section.project_id==project_id).first()
    if not s:
        raise HTTPException(404, 'Section not found')
    prompt = f'Write content for section "{s.title}" in project {project_id}.'
    out = llm.send(prompt, context={'section':s.title})
    s.content = out
    db.add(s); db.commit()
    return {'section_id': s.id, 'content': out}

@router.post('/project/{project_id}/section/{section_id}/refine')
def refine_section(project_id:int, section_id:int, payload:dict, db: Session = Depends(get_db)):
    s = db.query(models.Section).filter(models.Section.id==section_id, models.Section.project_id==project_id).first()
    if not s:
        raise HTTPException(404, 'Section not found')
    prompt = payload.get('prompt','Refine content')
    out = llm.send(prompt, context={'section':s.title, 'current': s.content})
    s.content = out
    db.add(s); db.commit()
    return {'section_id': s.id, 'content': out}
