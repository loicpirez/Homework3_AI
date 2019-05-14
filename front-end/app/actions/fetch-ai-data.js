import axios from 'axios'

export const FETCH_AI_DATA = 'FETCH_AI_DATA'
export const FETCHED_AI_DATA = 'FETCHED_AI_DATA'
export const ERROR_FETCH_AI_DATA = 'ERROR_FETCH_AI_DATA'

export function fetchAIdata () {
  return (dispatch) => {
    const url = 'http://localhost:5000/'
    axios.get(url).then(response => {
      dispatch(fetchedAIdata(response.data))
    })
      .catch(error => {
        throw error
      })

    return {
      type: FETCH_AI_DATA
    }
  }
}

export function fetchedAIdata (data) {
  return {
    type: FETCHED_AI_DATA,
    payload: data
  }
}
