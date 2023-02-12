import axios from "axios";
import { Test } from "./types";

const instance = axios.create({
    baseURL: '/api'
});

export const postTest = async (test: Test) => {
    return await instance.post('/test', test)
}

export const getTests = async (): Promise<Test[]> => {
    const response = await instance.get('/tests')

    return response.data as Test[];
};
