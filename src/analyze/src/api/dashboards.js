import axios from 'axios';
import utils from './utils';

export default {
  getDashboards() {
    return axios.get(utils.buildUrl('dashboards', 'all'));
  },
  getDashboard(id) {
    return axios.get(utils.buildUrl('dashboards', `dashboard/${id}`));
  },
  saveDashboard(data) {
    return axios.post(utils.buildUrl('dashboards', 'save'), data);
  },
};
