import React from 'react'
import PropTypes from 'prop-types'
import { withStyles } from '@material-ui/core/styles'
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import Button from '@material-ui/core/Button'
import { fetchAIdata } from '../actions'
import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'
import * as FetchAIActions from '../actions/fetch-ai-data'

const styles = {
  root: {
    flexGrow: 1
  },
  grow: {
    flexGrow: 1
  },
  menuButton: {
    marginLeft: -12,
    marginRight: 20
  }
}

class SimpleAppBar extends React.Component {
  constructor (props) {
    super(props)
    console.log(props)
  }

  render () {
    return (
      <div className={this.props.classes.root}>
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6" className={this.props.classes.grow} color="inherit">⚾ Baseball Players Rentability</Typography>
            <Button color="inherit" onClick={this.props.fetchAIdata}>Get data from A.I</Button>
          </Toolbar>
        </AppBar>
      </div>
    )
  }
}

function mapDispatchToProps (dispatch) {
  return bindActionCreators(FetchAIActions, dispatch)
}

export default connect(null, mapDispatchToProps)(withStyles(styles)(SimpleAppBar))
