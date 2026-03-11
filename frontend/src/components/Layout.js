import InteractionForm from "./InteractionForm";
import AIChat from "./AIChat";
import "../App.css";

function Layout(){

  return(

    <div className="dashboard">

      {/* Sidebar */}

      <div className="sidebar">

        <div className="logo">
          HCP CRM
        </div>

        <div className="menu-item">
          Dashboard
        </div>

        <div className="menu-item">
          Interactions
        </div>

        <div className="menu-item">
          Prompt History
        </div>

        <div className="menu-item">
          Analytics
        </div>

      </div>


      {/* Main */}

      <div className="main">

        <div className="card">
          <InteractionForm/>
        </div>

        <div className="card">
          <AIChat/>
        </div>

      </div>

    </div>

  );

}

export default Layout;