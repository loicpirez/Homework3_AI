// @flow
import React, { Component } from 'react';
import MuiThemeProvider from '@material-ui/core/styles/MuiThemeProvider';
import Home from '../components/Home';
import theme from '../mui-theme';

type Props = {};

export default class HomePage extends Component<Props> {
  props: Props;

  render() {
    return (
      <MuiThemeProvider theme={theme}>
        <Home />
      </MuiThemeProvider>
    );
  }
}
