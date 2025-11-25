from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.services.docx_exporter import build_docx
from app.services.pptx_exporter import build_pptx
from fastapi.responses import FileResponse
import os, tempfile

router = APIRouter()

@router.get('/project/{project_id}')
def export_project(project_id:int, format:str='docx', db: Session = Depends(get_db)):
    p = db.query(models.Project).filter(models.Project.id==project_id).first()
    if not p:
        raise HTTPException(404,'Project not found')
    sections = p.sections
    tmpdir = tempfile.gettempdir()
    filename = os.path.join(tmpdir, f'project_{project_id}.{format}')
    if format=='pptx' or p.doc_type=='pptx':
        build_pptx(p, filename)
    else:
        build_docx(p, filename)
    return FileResponse(filename, media_type='application/octet-stream', filename=os.path.basename(filename))
