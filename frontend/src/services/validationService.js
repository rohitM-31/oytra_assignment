
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const validateAddress = async (customerDetails) => {
  const response = await axios.post(
    `${API_URL}/validate-address`,
    customerDetails
  );

  return response.data;
};
