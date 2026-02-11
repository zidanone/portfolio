import axios from 'axios';

const API = axios.create({
  baseURL: 'portfolio-b4be.onrender.com/api/',
});

export const getOverview = () => API.get('overview/');
export const getProfile = () => API.get('profile/');
export const getSkills = () => API.get('skills/');
export const getProjects = () => API.get('projects/');
export const getExperiences = () => API.get('experiences/');
export const getEducation = () => API.get('education/');
export const sendContactMessage = (data) => API.post('contact/', data);

export default API;
