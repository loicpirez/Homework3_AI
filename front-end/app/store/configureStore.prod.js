// @flow
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { createHashHistory } from 'history';
import { routerMiddleware } from 'connected-react-router';
import createRootReducer from '../reducers';
import * as fetchAIDataActions from '../actions/fetch-ai-data.js';
import type { fetchAIDataStateType } from '../reducers/types';

const history = createHashHistory();
const rootReducer = createRootReducer(history);
const router = routerMiddleware(history);
const enhancer = applyMiddleware(thunk, router);

function configureStore(initialState?: fetchAIDataStateType) {
  return createStore<*, fetchAIDataStateType, *>(
    rootReducer,
    initialState,
    enhancer
  );
}

export default { configureStore, history };
