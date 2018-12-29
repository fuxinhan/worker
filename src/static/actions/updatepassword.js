import axios from 'axios'
import { push } from 'react-router-redux';
import { SERVER_URL } from '../utils/config';
import {
    REGIST_USER_FAILURE,
    REGIST_USER_REQUEST,
    REGIST_USER_SUCCESS,
    SEND_CODE_REQUEST,
} from '../constants/index'

export function registerUserSuccess( mobile){
    sessionStorage.setItem('mobile', JSON.stringify(mobile))
    return {
        type: REGIST_USER_SUCCESS,
        payload: {
            mobile
        }
    }
}

export function registerUserFailure(error, message) {
    sessionStorage.removeItem('token')
    return {
        type: REGIST_USER_FAILURE,
        payload: {
            status: error,
            statusText: message
        }
    }
}

export function registerUserRequest() {
    return {
        type: REGIST_USER_REQUEST
    }
}

export function sendCodesRequest() {
    return {
        type: SEND_CODE_REQUEST
    }
}

export function sendCodes(mobile) {
    return (dispatch) => {
        dispatch(sendCodesRequest())
        return axios({
            method: 'POST',
            url: `${SERVER_URL}/api/smscode/`,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            data: {
                mobile: `${mobile}`,
            }
    }).then((resp) => {
            console.log("send code success, 返回的数据是: ", resp.data)
    }).catch((error) => {
        if (error && typeof error.response !== 'undefined' && error.response.status === 401) {
            // Invalid authentication credentials
            return error.response.json().then((data) => {
                dispatch(registerUserFailure(401, data.non_field_errors[0]));
            });
        } else if (error && typeof error.response !== 'undefined' && error.response.status >= 500) {
            // Server side error
            dispatch(registerUserFailure(500, 'A server error occurred while sending your data!'));
        } else {
            // Most likely connection issues
            dispatch(registerUserFailure('Connection Error', 'An error occurred while sending your data!'));
        }
        console.log(error.response)
        return Promise.resolve(); // TODO: we need a promise here because of the tests, find a better way
        });
    }
}

export function registerUser(mobile, code, password, redirect = '/login') {
    return (dispatch) => {
        dispatch(registerUserRequest())
        return axios({
            method: 'PUT',
            url: `${SERVER_URL}/api/users/`,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            data: {
                code: `${code}`,
                username:`${mobile}`,
                mobile:`${mobile}`,
                password: `${password}`,
            }
        }).then((resp) => {
            if (resp.status === 200 && resp.data.id){
                dispatch(registerUserSuccess( resp.data.mobile))
                dispatch(push(redirect))
            }else if(resp.data.error){
                alert(resp.data.error)
            }
            console.log("registerUser resp: ", resp)
            console.log("this is error",resp.data.error)
        }).catch((error) => {
            if (error && typeof error.response !== 'undefined' && error.response.status === 401) {
                // Invalid authentication credentials
                return error.response.json().then((data) => {
                    dispatch(registerUserFailure(401, data.non_field_errors[0]));
                });
            } else if (error && typeof error.response !== 'undefined' && error.response.status >= 500) {
                // Server side error
                dispatch(registerUserFailure(500, 'A server error occurred while sending your data!'));
            } else {
                // Most likely connection issues
                dispatch(registerUserFailure('Connection Error', 'An error occurred while sending your data!'));
            }
            console.log('error', error)
            return Promise.resolve(); // TODO: we need a promise here because of the tests, find a better way
        });
    }
}
