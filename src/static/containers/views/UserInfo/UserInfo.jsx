/* eslint-disable */
import React from "react";
// nodejs library that concatenates classes
import classNames from "classnames";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
import InputAdornment from "@material-ui/core/InputAdornment";
import DoneAll from "@material-ui/icons/DoneAll";
import AttachMoney from '@material-ui/icons/AttachMoney'

// core components
import Footers from "../components/Footers.jsx";
import GridContainer from "../../../components/Grid/GridContainer.jsx";
import GridItem from "../../../components/Grid/GridItem.jsx";
import CustomInput from '../../../components/CustomInput/CustomInput'
import Badge from "../../../components/Badge/Badge.jsx";
import Parallax from "../../../components/Parallax/Parallax.jsx";
import Button from "../../../components/CustomButtons/Button.jsx";
import profilePageStyle from "../../../../assets/jss/material-kit-pro-react/views/profilePageStyle.jsx";
import MyHeader from '../components/MyHeader'
import CircularProgress from '@material-ui/core/CircularProgress';
import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'
import PropTypes from 'prop-types'
import * as actionCreators from '../../../actions/UserInfo'

import cardBlog5 from '../../../../assets/img/bg.jpg'

class UserinfoView extends React.Component {

  static propTypes = {
    dispatch: PropTypes.func.isRequired,
    isFetching: PropTypes.bool.isRequired,
    data: PropTypes.object,
    token: PropTypes.string.isRequired,
    action: PropTypes.shape({
      getUserDataFetch: PropTypes.func.isRequired
    })
  }

  static defaultProps = {
    data: '' 
  };

  componentWillMount() {
    const token = this.props.token
    this.props.actions.getUserDataFetch(token)
  }

  render() {
    const { classes, data, isFetching, ...rest } = this.props;
    return (
      <div>
        <MyHeader />

        <Parallax
          image={require("../../../../assets/img/examples/city.jpg")}
          filter="dark"
          className={classes.parallax}
        />
        <div className={classNames(classes.main, classes.mainRaised)}>
          {data === null ?
            <CircularProgress className={classes.progress} color="secondary" size={50} /> :

            <div className={classes.container}>
              <GridContainer>
                <GridItem xs={12} sm={12} md={12}>
                  <header className={classes.headerInfo}>
                    <div className={classes.headerLeft}>
                      <div style={{
                          backgroundImage: `url(${cardBlog5})`
                        }} className={classes.headerLeftIcon}></div>
                      <div className={classes.headerName}>
                        <div className={classes.headerNameT}>{data.name}</div>
                        <Badge color="warning" className={classes.headerB}>新手过招</Badge>
                        <Badge color="primary" className={classes.headerB}>学生</Badge>
                      </div>
                    </div>
                    <div className={classes.headerRight}>
                      <Button color="primary" round>
                        <DoneAll/> 关注
                      </Button>
                    </div>
                  </header>
                </GridItem>
                <GridItem xs={12} sm={12} md={4}>
                  <h4 style={{color:"#DC143C"}}>基本信息</h4>
                  <div className={classes.bodyLeft}>
                    <span>昵称</span>
                    <CustomInput
                      labelText={data.name}
                      id="float"
                      formControlProps={{
                        fullWidth: true
                      }}
                      // inputProps={{
                      //   onChange: event => this.change(event, "name"),
                      //   type: "text",ActionCreators
                      //   startAdornment: (
                      //     <InputAdornment position="start" />
                      //   )
                      // }}
                    />
                    <span>性别</span>
                    <CustomInput
                      labelText={data.gender}
                      id="float"
                      formControlProps={{
                        fullWidth: true
                      }}
                      // inputProps={{
                      //   onChange: event => this.change(event, "gender"),
                      //   type: "text",
                      //   startAdornment: (
                      //     <InputAdornment position="start" />
                      //   )
                      // }}
                    />
                    <span>年龄</span>
                    <CustomInput
                      labelText={data.birthday}
                      id="float"
                      formControlProps={{
                        fullWidth: true
                      }}
                      // inputProps={{
                      //   onChange: event => this.change(event, "birthday"),
                      //   type: "text",
                      //   startAdornment: (
                      //     <InputAdornment position="start" />
                      //   )
                      // }}
                    />
                    <span>QQ / 微信</span>
                    <CustomInput
                      labelText={data.username.substr(0,3)+"****"+data.username.substr(7)}
                      id="float"
                      formControlProps={{
                        fullWidth: true
                      }}
                    />
                    <p>手机号 ： {data.username.substr(0,3)+"****"+data.username.substr(7)}</p>
                    <hr/>
                    <div className={classes.textCenter}>
                      <Button color="primary" round>
                        提交保存
                      </Button>
                    </div>
                    
                  </div>
                </GridItem>
                <GridItem xs={12} sm={12} md={4}>
                  <h4 style={{color:"#DC143C"}}>我的荣誉</h4>
                  <div className={classes.center}>
                    <span>我的瓦力币</span>
                    <div className={classes.centerMoney}>
                      <div className={classes.moneyTop}>
                        <AttachMoney/> 
                        <span>50</span>
                        <hr/>
                        <p>如何获取瓦力币？</p>
                        <div>1 .  通过线下和线上课程完成老师的任务。<br/>2 .   还可以创作分享自己的作品来</div>
                      </div>
                    </div>
                  </div>
                  
                </GridItem>
                <GridItem xs={12} sm={12} md={4}>
                  <h4 style={{color:"#DC143C"}}>自我介绍</h4>
                  <div className={classes.bodyRight}>
                      <span>关于我</span>
                      <div className={classes.rightTop}>
                        <textarea></textarea>
                      </div>
                  </div>
                </GridItem>
              </GridContainer>
            </div>
          }
        </div>

        <Footers />
      </div>
    );
  }
}
const mapStateToProps = (state) => {
  return {
      data: state.userdata.data,
      isFetching: state.userdata.isFetching
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    dispatch,
    actions: bindActionCreators(actionCreators, dispatch)
  }
}

const UserInfo =  withStyles(profilePageStyle)(UserinfoView)

export default connect(mapStateToProps, mapDispatchToProps)(UserInfo)
