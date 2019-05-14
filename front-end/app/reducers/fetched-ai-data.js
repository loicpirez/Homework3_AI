// @flow
import { FETCHED_AI_DATA } from '../actions/fetch-ai-data'
import type { Action } from './types';

export default function fetchedAIdata(state: {}, action: Action) {
  switch (action.type) {
    case FETCHED_AI_DATA:
      return { data: action.payload}
    default:
      return state
  }
}
