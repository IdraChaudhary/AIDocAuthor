from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, Base, engine
from app import models, schemas
from typing import List
from pydantic import BaseModel

# create tables on startup (for demo)
Base.metadata.create_all(bind=engine)

router = APIRouter()

# simple dependency (no real auth for demo)
def get_current_user(db: Session = Depends(get_db)):
    user = db.query(models.User).first()
    if not user:
        # create demo user
        user = models.User(email='demo@example.com', hashed_password='x')
        db.add(user); db.commit(); db.refresh(user)
    return user

@router.post('/', response_model=dict)
def create_project(p: schemas.ProjectCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    proj = models.Project(title=p.title, doc_type=p.doc_type, owner_id=user.id)
    db.add(proj); db.commit(); db.refresh(proj)
    for i, s in enumerate(p.sections or []):
        sec = models.Section(title=s.title, content='', order=i, project_id=proj.id)
        db.add(sec)
    db.commit()
    return {'project_id': proj.id}

@router.get('/', response_model=list)
def list_projects(db: Session = Depends(get_db), user = Depends(get_current_user)):
    projs = db.query(models.Project).filter(models.Project.owner_id==user.id).all()
    out = []
    for p in projs:
        out.append({'id':p.id, 'title':p.title, 'doc_type':p.doc_type})
    return out

@router.get('/{project_id}', response_model=dict)
def get_project(project_id:int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    p = db.query(models.Project).filter(models.Project.id==project_id, models.Project.owner_id==user.id).first()
    if not p:
        raise HTTPException(404, 'Not found')
    sections = [{'id':s.id,'title':s.title,'content':s.content,'order':s.order} for s in p.sections]
    return {'id':p.id,'title':p.title,'doc_type':p.doc_type,'sections':sections}
