import type { Dispatch as ReduxDispatch, Store as ReduxStore } from 'redux';

export type fetchAIDataStateType = {
  +data: object
};

export type Action = {
  +type: string
};

export type GetState = () => fetchAIDataStateType;

export type Dispatch = ReduxDispatch<Action>;

export type Store = ReduxStore<GetState, Action>;
