import React from 'react';
// nodejs library that concatenates classes
import classNames from 'classnames';
// nodejs library to set properties for components
import PropTypes from 'prop-types';
// @material-ui/core components
import { withStyles } from '@material-ui/core/styles'
// core components
import parallaxStyle from '../../../assets/jss/material-kit-pro-react/components/parallaxStyle'

// https://www.cnblogs.com/laixiangran/p/8849887.html
class Parallax extends React.Component {
  constructor(props) {
    super(props);
    const windowScrollTop = ((document.documentElement
      || document.body.parentNode || document.body).scrollTop / 3)
    this.state = {
      transform: `translate3d(0,${windowScrollTop}px,0)`,
    };
    this.resetTransform = this.resetTransform.bind(this);
  }

  componentDidMount() {
    const windowScrollTop = ((document.documentElement
      || document.body.parentNode || document.body).scrollTop / 3)
    this.setState({
      transform: `translate3d(0,${windowScrollTop}px,0)`,
    });
    window.addEventListener('scroll', this.resetTransform);
  }

  componentWillUnmount() {
    window.removeEventListener('scroll', this.resetTransform);
  }

  resetTransform() {
    const windowScrollTop = ((document.documentElement
      || document.body.parentNode || document.body).scrollTop / 3)
    this.setState({
      transform: `translate3d(0,${windowScrollTop}px,0)`,
    });
  }

  render() {
    const {
      classes,
      filter,
      className,
      children,
      style,
      image,
      small,
    } = this.props;
    const parallaxClasses = classNames({
      [classes.parallax]: true,
      [classes[`${filter}Color`]]: filter !== undefined,
      [classes.small]: small,
      [className]: className !== undefined,
    });
    return (
      <div
        className={parallaxClasses}
        style={{
          ...style,
          backgroundImage: `url(${image})`,
          ...this.state,
        }}
        ref="parallax"
      >
        {children}
      </div>
    )
  }
}

Parallax.propTypes = {
  classes: PropTypes.object.isRequired,
  className: PropTypes.string,
  filter: PropTypes.oneOf([
    'primary',
    'rose',
    'dark',
    'info',
    'success',
    'warning',
    'danger',
  ]),
  children: PropTypes.node,
  style: PropTypes.string,
  image: PropTypes.string,
  small: PropTypes.bool,
};

export default withStyles(parallaxStyle)(Parallax);
