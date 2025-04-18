import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export const sendMessage = (message) => {
  return axios.post(`${API_BASE_URL}/fact-check`, { query: message });
};
