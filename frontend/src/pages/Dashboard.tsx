import React, {useEffect, useState} from 'react'
import axios from 'axios'

export default function Dashboard(){
    const [projects, setProjects] = useState([])
    useEffect(()=>{
        axios.get('http://localhost:8000/projects').then(r=>setProjects(r.data)).catch(()=>{})
    },[])
    return <div className='p-6 max-w-4xl mx-auto'>
        <h1 className='text-2xl font-bold mb-4'>AI Doc Platform - Dashboard (Frontend)</h1>
        <div className='space-y-3'>
            {projects.length===0 ? <div className='text-gray-600'>No projects yet (create via backend API)</div> : projects.map(p=> <div key={p.id} className='p-3 border rounded'>{p.title} ({p.doc_type})</div>)}
        </div>
    </div>
}
