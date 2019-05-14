import React from 'react'
import PropTypes from 'prop-types'
import { withStyles } from '@material-ui/core/styles'
import Paper from '@material-ui/core/Paper'
import Grid from '@material-ui/core/Grid'

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

function MoneyContainer (props) {
  const { classes } = props

  return (
    <Grid container spacing={24} >
      <Grid item xs>
        <Paper className={classes.paper}>Initial amount of money: <b>...€</b></Paper>
      </Grid>
      <Grid item xs>
        <Paper className={classes.paper}>Total invested: <b>...€</b></Paper>
      </Grid>
    </Grid>
  )
}

MoneyContainer.propTypes = {
  classes: PropTypes.object.isRequired
}

export default withStyles(styles)(MoneyContainer)