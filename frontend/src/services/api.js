import axios from 'axios';

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

export const identifyCar = async (imageFile) => {
  const formData = new FormData();
  formData.append('file', imageFile, 'car.jpg');
  
  const response = await axios.post(`${BACKEND_URL}/predict`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
    timeout: 20000,
  });
  
  return response.data;
};

export const getCarSpecs = async (predClass) => {
  const response = await axios.get(`${BACKEND_URL}/car-specs`, {
    params: { pred_class: predClass },
    timeout: 20000,
  });
  
  return response.data;
};
