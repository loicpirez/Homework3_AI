import { createMuiTheme } from '@material-ui/core/styles'
import red from '@material-ui/core/colors/red'

export default createMuiTheme({
  palette: {
    primary: red
  },
  typography: {
    useNextVariants: true
  },
  overrides: {
    MuiFab: {
      root: {
        position: 'absolute',
        bottom: '2rem',
        right: '2rem'
      }
    }
  }
})
