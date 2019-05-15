import React from 'react'
import PropTypes from 'prop-types'
import { withStyles } from '@material-ui/core/styles'
import Paper from '@material-ui/core/Paper'
import Grid from '@material-ui/core/Grid'
import { connect } from 'react-redux'

const styles = theme => ({
  root: {
    flexGrow: 1
  },
  paper: {
    padding: theme.spacing.unit * 2,
    textAlign: 'center',
    color: theme.palette.text.secondary
  }
})

class MoneyContainer extends React.Component {
  componentWillReceiveProps (nextProps) {
    // You don't have to do this check first, but it can help prevent an unneeded render
    if (nextProps.AIdata !== this.state.AIdata) {
      console.log(nextProps.AIdata.money)
      this.setState({
        money_left: nextProps.AIdata.money.total,
        money_total: nextProps.AIdata.money.left
      })
    }
  }

  constructor (props) {
    super(props)
    this.state = {
      money_left: '...',
      money_total: '...'
    }
  }

  render () {
    return (
      <Grid container spacing={24} >
        <Grid item xs>
          <Paper className={this.props.classes.paper}>Initial amount of money: <b>{this.state.money_left} €</b></Paper>
        </Grid>
        <Grid item xs>
          <Paper className={this.props.classes.paper}>Total invested: <b>{this.state.money_total} €</b></Paper>
        </Grid>
      </Grid>
    )
  }
}

MoneyContainer.propTypes = {
  classes: PropTypes.object.isRequired
}

const mapStateToProps = state => {
  return {
    AIdata: state.fetchedAIdata.data
  }
}

export default connect(
  mapStateToProps,
  null
)(withStyles(styles)(MoneyContainer))
