import AIChat from "./components/AIChat"
import InteractionForm from "./components/InteractionForm"

function App(){

 return(

  <div style={{display:"flex"}}>

   <div style={{width:"70%"}}>
     <InteractionForm/>
   </div>

   <div style={{width:"30%"}}>
     <AIChat/>
   </div>

  </div>

 )
}

export default App