import axios from 'axios'
import { SERVER_URL } from '../utils/config'


export const getCoursesDataFetch = () => {

    return axios.get(`${SERVER_URL}/api/courses/`,{
        headers:{
            Accept: 'application/json'
        }
    }).then((response) => {
        console.log("this is courses"+response.data)
    }).catch((error) => {
        console.log(error.response)
        return Promise.resolve();

    })
}