import { createSlice } from "@reduxjs/toolkit";

const interactionSlice = createSlice({
  name: "interaction",
  initialState: {
    formData: {}
  },
  reducers: {
    setFormData: (state, action) => {
      state.formData = action.payload;
    }
  }
});

export const { setFormData } = interactionSlice.actions;
export default interactionSlice.reducer;