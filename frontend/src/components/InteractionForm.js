import { useSelector } from "react-redux";

function InteractionForm() {

  const data = useSelector(state => state.interaction.formData) || {};

  return (

    <div className="card">

      <div className="title">Log HCP Interaction</div>

      <label>HCP Name</label>
      <input
        value={data?.hcp_name || ""}
        readOnly
      />

      <label>Interaction Type</label>
      <input
        value={data?.interaction_type || ""}
        readOnly
      />

      <label>Topics Discussed</label>
      <input
        value={data?.topics_discussed || ""}
        readOnly
      />

      <label>Sentiment</label>
      <input
        value={data?.sentiment || ""}
        readOnly
      />

      <label>Materials Shared</label>
      <input
        value={
          Array.isArray(data?.materials_shared)
            ? data.materials_shared.join(", ")
            : data?.materials_shared || ""
        }
        readOnly
      />

      <label>Follow Up</label>
      <input
        value={data?.follow_up || ""}
        readOnly
      />

    </div>

  );

}

export default InteractionForm;