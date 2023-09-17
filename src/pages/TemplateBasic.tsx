import { Idata } from "../interfaces";
import ContactInfo from "../components/ContactInfo";



const TemplateBasic = ({ dataJSON } : {dataJSON :Idata}) => {
  return (
  <div>
    <header>
			<ContactInfo {...dataJSON.contact}/>
		</header>
		<main>
			<p>Template Basic</p>
		</main>
  </div>
  )
}

export default TemplateBasic;