//import { useState } from 'react'
import TemplateBasic from './pages/TemplateBasic'
//import './App.css'
import data from '../data/cv_data.json'
import { Idata } from './interfaces';

function App() {
  //const [count, setCount] = useState(0)
  const dataJSON : Idata = data;
  return (
    <div>
      <TemplateBasic dataJSON={dataJSON}/>
    </div>
    );
}

export default App
