import axios from "axios";
import { useDispatch } from "react-redux";
import { setFormData } from "../redux/interactionSlice";
import { useState } from "react";

function AIChat(){

  const [prompt,setPrompt] = useState("");

  const dispatch = useDispatch();

  const sendPrompt = async () => {

    console.log("Button clicked");

    if(!prompt){
      alert("Please enter interaction text first");
      return;
    }

    try{

      const res = await axios.post(
        "http://127.0.0.1:8000/ai-extract",
        { prompt: prompt }
      );

      console.log("API Response:",res.data);

      dispatch(setFormData(res.data.data));

    }
    catch(error){

      console.log("API error:",error);

      alert("Backend not responding or API error");

    }

  };

  return(

    <div>

      <div className="title">AI Assistant</div>

      <label>Describe your interaction</label>

      <textarea
        rows="6"
        placeholder="Example: Met Dr Sharma today and discussed diabetes drug..."
        value={prompt}
        onChange={(e)=>setPrompt(e.target.value)}
      />

      <button type="button" onClick={sendPrompt}>
        Log Interaction
      </button>

    </div>

  );

}

export default AIChat;