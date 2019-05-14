// @flow
import { combineReducers } from 'redux';
import { connectRouter } from 'connected-react-router';
import fetchedAIdata from './fetched-ai-data';

export default function createRootReducer(history: History) {
  return combineReducers<{}, *>({
    router: connectRouter(history),
    fetchedAIdata
  });
}
