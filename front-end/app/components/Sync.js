import React from 'react'
import PropTypes from 'prop-types'
import { withStyles } from '@material-ui/core/styles'
import Fab from '@material-ui/core/Fab'
import SyncSharpIcon from '@material-ui/icons/SyncSharp'
import Icon from '@material-ui/core/Icon'
import DeleteIcon from '@material-ui/icons/Delete'
import NavigationIcon from '@material-ui/icons/Navigation'

const styles = theme => ({
  fab: {
    margin: theme.spacing.unit
  },
  extendedIcon: {
    marginRight: theme.spacing.unit
  }
})

function Sync (props) {
  const { classes } = props
  return (
    <div>
      {/* <Fab color="primary" aria-label="Sync" className={classes.fab}>
        <SyncSharpIcon />
      </Fab> */}
    </div>
  )
}

Sync.propTypes = {
  classes: PropTypes.object.isRequired
}

export default withStyles(styles)(Sync)
