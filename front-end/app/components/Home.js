// @flow
import React, { Component } from 'react';
// import { Link } from 'react-router-dom';
// import routes from '../constants/routes';
import styles from './Home.css';
import SimpleAppBar from './SimpleAppBar';
import EnhancedTable from './EnhancedTable'
import Sync from './Sync'
import MoneyContainer from './MoneyContainer'
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';

type Props = {};

export default class Home extends Component<Props> {
  props: Props;

  render() {
    return (
      <div className={styles.container} data-tid="container">
        <SimpleAppBar />
        <div style={{ padding: 20 }}>
          <Grid container spacing={24}>
            <Grid item xs={12}>
              <EnhancedTable />
            </Grid>
            <Grid item xs={12}>
              <MoneyContainer />
            </Grid>
          </Grid>
        </div>
        <Sync />
        {/* <h2>Home</h2>
        <Link to={routes.COUNTER}>azeaze Counter</Link> */}
      </div>
    );
  }
}
