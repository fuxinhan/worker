import React from "react";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
import InputAdornment from "@material-ui/core/InputAdornment";
import Checkbox from "@material-ui/core/Checkbox";
import FormControlLabel from "@material-ui/core/FormControlLabel";
// @material-ui/icons
import Timeline from "@material-ui/icons/Timeline";
import Code from "@material-ui/icons/Code";
import Group from "@material-ui/icons/Group";

import LockOutlined from "@material-ui/icons/LockOutlined";
import Check from "@material-ui/icons/Check";
import Phone from "@material-ui/icons/Phone"
import Message from "@material-ui/icons/Message"

import { Link } from "react-router-dom";
// core components
// import HeaderLinks from "../../../components/Header/HeaderLinks.jsx";
import Footers from "../components/Footers.jsx";
import GridContainer from "../../../components/Grid/GridContainer.jsx";
import GridItem from "../../../components/Grid/GridItem.jsx";
import Button from "../../../components/CustomButtons/Button.jsx";
import Card from "../../../components/Card/Card.jsx";
import CardBody from "../../../components/Card/CardBody.jsx";
import InfoArea from "../../../components/InfoArea/InfoArea.jsx";
import CustomInput from "../../../components/CustomInput/CustomInput.jsx";

import signupPageStyle from "../../../../assets/jss/material-kit-pro-react/views/signupPageStyle";
import MyHeader from '../components/MyHeader'

import image from "../../../../assets/img/bg7.jpg";
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import * as actionCreators from '../../../actions/updatepassword';

class PasswordView extends React.Component {
    static propTypes = {
        dispatch: PropTypes.func.isRequired,
        statusText: PropTypes.string,
        actions: PropTypes.shape({
            sendCodes: PropTypes.func.isRequired,
            registerUser: PropTypes.func.isRequired,
        }).isRequired,
        location: PropTypes.shape({
            search: PropTypes.string.isRequired
        })
    };

    static defaultProps = {
        statusText: '',
        location: null
    };

  constructor(props) {
    super(props);
    const redirectRoute = this.props.location ? this.extractRedirect(this.props.location.search) || '/' : '/';

    this.state = {
      liked:true,
      count:60,
      checked: [1],
      redirectTo: redirectRoute,
      mobile: '',
      password: '',
      code: '',

      mobileState: '',
      passwordState: '',
      codeState: '',
    };
    this.handleToggle = this.handleToggle.bind(this);
  }
  handleToggle(value) {
    const { checked } = this.state;
    const currentIndex = checked.indexOf(value);
    const newChecked = [...checked];

    if (currentIndex === -1) {
      newChecked.push(value);
    } else {
      newChecked.splice(currentIndex, 1);
    }

    this.setState({
      checked: newChecked
    });
  }
  componentDidMount() {
    window.scrollTo(0, 0);
    document.body.scrollTop = 0;
  }

  extractRedirect = (string) => {
    const match = string.match(/next=(.*)/);
    return match ? match[1] : '/';
  };
  sendcode = (e) => {
    console.log(this.state.mobile)
    e.preventDefault();
     this.props.actions.sendCodes(this.state.mobile)
        .catch((error) => {
            console.log("sendCodes出错")
            console.log(error);
        })
        if (this.state.liked) {
          const timer = setInterval( ()=> {
              var count = this.state.count;
              this.state.liked = false;
              count -= 1;
              if (count < 1) {
                this.setState({liked: true});
                count = 60;
                clearInterval(timer);
            }
            this.setState({
                count: count
            });
          },1000);
        }
        return
  };

    // 验证手机号
    verifyPhone(value) {
        var phoneRex = /(^1[34578]\d{9}$|^147\d{8}$|^176\d{8}$)/;
        if (phoneRex.test(value)) {
          return true;
        }
        return false;
      }

    // 验证长度，密码不得少于6个字符
    verifyLength(value, length) {
        if (value.length >= length) {
          return true;
        }
        return false;
    }

    change(event, stateName, type, stateNameEqualTo) {
        switch (type) {
          case "phone":
            if (this.verifyPhone(event.target.value)) {
              this.setState({ [stateName + "State"]: "success" });
            } else {
              this.setState({ [stateName + "State"]: "error" });
            }
            break;
          case "length":
            if (this.verifyLength(event.target.value, stateNameEqualTo)) {
              this.setState({ [stateName + "State"]: "success" });
            } else {
              this.setState({ [stateName + "State"]: "error" });
            }
            break;
          default:
            break;
        }
        this.setState({ [stateName]: event.target.value });
      }

      isValidated() {
        if (
          this.state.mobileState === "success" &&
          this.state.passwordState === "success" &&
          this.state.codeState === "success"
        ) {
          return true;
        } else {
          if (this.state.mobileState !== "success") {
            this.setState({ mobileState: "error" });
          }
          if (this.state.passwordState !== "success") {
            this.setState({ passwordState: "error" });
          }
          if (this.state.codeState !== "success") {
            this.setState({ codeState: "error" });
          }
        }
        return false;
      }

      register = (e) => {
        e.preventDefault();
        return this.props.actions.registerUser(this.state.mobile, this.state.code, this.state.password, this.state.redirectTo)
            .catch((error) => {
                console.log(error);
            })
    };

  render() {
    const { classes, ...rest } = this.props;
    const  text = this.state.liked ? '获取验证码' : this.state.count + '秒后重发'
    return (
      <div>
        <MyHeader />
        <div
          className={classes.pageHeader}
          style={{
            backgroundImage: "url(" + image + ")",
            backgroundSize: "cover",
            backgroundPosition: "top center"
          }}
        >
          <div className={classes.container}>
            <GridContainer justify="center">
              <GridItem xs={12} sm={10} md={10}>
                <Card className={classes.cardSignup}>
                  <h2 className={classes.cardTitle}>Register</h2>
                  <CardBody>
                    <GridContainer justify="center">
                      <GridItem xs={12} sm={5} md={5}>
                        <InfoArea
                          className={classes.infoArea}
                          title="大颗粒课程"
                          description="以《幼儿园教育指导纲要》，让孩子在动手实践中学习科学、数学、社会领域的知识。"
                          icon={Timeline}
                          iconColor="rose"
                        />
                        <InfoArea
                          className={classes.infoArea}
                          title="积木机器人课程"
                          description='机器人器材在乐高积木基础上，增加了CPU、马达、触碰传感器、红外线传感器等电子原件，赋予机器人"生命"。'
                          icon={Code}
                          iconColor="primary"
                        />
                        <InfoArea
                          className={classes.infoArea}
                          title="单片机机器人课程"
                          description="机器人采用印刷电路板作为主要结构，课程着重培养孩子逻辑思维能力，提高孩子认识事物、分析事物、解决事物的能力。"
                          icon={Group}
                          iconColor="info"
                        />
                      </GridItem>
                      <GridItem xs={12} sm={5} md={5}>
                        <div className={classes.textCenter}>
                          <Button justIcon round color="twitter">
                            <i
                              className={classes.socials + " fa fa-weixin"}
                            />
                          </Button>
                          {` `}
                          <Button justIcon round color="dribbble">
                            <i
                             className={classes.socials + " fa fa-qq"}
                           />
                          </Button>
                          {` `}
                          <Button justIcon round color="facebook">
                            <i
                              className={classes.socials + " fa fa-weibo"}
                            />
                          </Button>
                          {` `}
                          <p className={classes.socialTitle}>
                            已经拥有账号！去<Link to="/login">登陆</Link>
                          </p>
                        </div>
                        <form className={classes.form}>
                          
                          <CustomInput
                          success={this.state.mobileState === "success"}
                        error={this.state.mobileState === "error"}
                        id="phone"
                        formControlProps={{
                          fullWidth: true
                        }}
                        inputProps={{
                            onChange: event => this.change(event, "mobile","phone"),
                          placeholder: "Phone...",
                          type: "phone",
                          startAdornment: (
                            <InputAdornment position="start">
                              <Phone className={classes.inputIconsColor} />
                            </InputAdornment>
                          )
                        }}
                      />
                      <CustomInput
                        success={this.state.codeState === "success"}
                        error={this.state.codeState === "error"}

                        id="code"
                        formControlProps={{
                          fullWidth: true
                        }}
                        inputProps={{
                          onChange: event => this.change(event, "code", "length", 4),

                          placeholder: "Code...",
                          type: "code",
                          startAdornment: (
                            <InputAdornment position="start">
                              <Message className={classes.inputIconsColor} />
                            </InputAdornment>
                          ),
                          endAdornment: (
                            <InputAdornment position="end">
                                {/* <Send /> */}
                                <Button color="primary" onClick={this.sendcode}  disabled={!this.state.liked}>
                                  {text}
                                </Button>
                            </InputAdornment>
                          )
                        }}
                      />

                          <CustomInput
                            success={this.state.passwordState === "success"}
                            error={this.state.passwordState === "error"}

                            formControlProps={{
                              fullWidth: true,
                              className: classes.customFormControlClasses
                            }}
                            inputProps={{
                                onChange: event => this.change(event, "password", "length", 6),

                              startAdornment: (
                                <InputAdornment
                                  position="start"
                                  className={classes.inputAdornment}
                                >
                                  <LockOutlined
                                    className={classes.inputAdornmentIcon}
                                  />
                                </InputAdornment>
                              ),
                              placeholder: "New Password..."
                            }}
                          />
                          <FormControlLabel
                            classes={{
                              label: classes.label
                            }}
                            control={
                              <Checkbox
                                tabIndex={-1}
                                onClick={() => this.handleToggle(1)}
                                checkedIcon={
                                  <Check className={classes.checkedIcon} />
                                }
                                icon={
                                  <Check className={classes.uncheckedIcon} />
                                }
                                classes={{
                                  checked: classes.checked
                                }}
                                checked={
                                  this.state.checked.indexOf(1) !== -1
                                    ? true
                                    : false
                                }
                              />
                            }
                            label={
                              <span>
                                I agree to the{" "}
                                <a href="#pablo">terms and conditions</a>.
                              </span>
                            }
                          />
                          <div className={classes.textCenter}>
                            <Button round color="primary" onClick={this.register}>
                              确认修改
                            </Button>
                          </div>
                        </form>
                      </GridItem>
                    </GridContainer>
                  </CardBody>
                </Card>
              </GridItem>
            </GridContainer>
          </div>
          <Footers/>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
    return {
        statusText: state.auth.statusText
    };
};

const mapDispatchToProps = (dispatch) => {
    return {
        dispatch,
        actions: bindActionCreators(actionCreators, dispatch)
    };
};

const UpdatePassword = connect(mapStateToProps, mapDispatchToProps)(PasswordView);
export default withStyles(signupPageStyle)(UpdatePassword);
