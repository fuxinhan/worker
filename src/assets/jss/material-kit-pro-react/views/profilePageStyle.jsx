import {
  container,
  cardTitle,
  title,
  mlAuto,
  mrAuto,
  main,
  mainRaised
} from "../../../../assets/jss/material-kit-pro-react.jsx";

import imagesStyle from "../../../../assets/jss/material-kit-pro-react/imagesStyles.jsx";

import tooltipsStyle from "../../../../assets/jss/material-kit-pro-react/tooltipsStyle.jsx";

const profilePageStyle = {
  container,
  ...imagesStyle,
  ...tooltipsStyle,
  cardTitleWhite: {
    ...cardTitle,
    color: "#FFFFFF !important"
  },
  cardTitle,
  profile: {
    textAlign: "center",
    "& img": {
      maxWidth: "160px",
      width: "100%",
      margin: "0 auto",
      transform: "translate3d(0, -50%, 0)"
    }
  },
  description: {
    margin: "1.071rem auto 0",
    maxWidth: "600px",
    color: "#999"
  },
  textCenter: {
    textAlign: "center !important"
  },
  name: {
    marginTop: "-80px"
  },

  main: {
    ...main
  },
  mainRaised: {
    ...mainRaised
  },
  title: {
    ...title,
    position: "relative",
    marginTop: "30px",
    minHeight: "32px",
    textDecoration: "none"
  },
  follow: {
    position: "absolute",
    top: "0",
    right: "0"
  },
  followIcon: {
    width: "20px",
    height: "20px"
  },
  followButton: {
    marginTop: "-28px !important"
  },
  gridItem: {
    ...mlAuto,
    ...mrAuto
  },
  collections: {
    marginTop: "20px"
  },
  cardBody: {
    display: "flex",
    boxOrient: "vertical",
    boxDirection: "normal",
    flexDirection: "column",
    boxPack: "center",
    justifyContent: "center"
  },
  badge: {
    display: "inline-table",
    margin: "0 auto"
  },
  listUnstyled: {
    paddingLeft: "0",
    listStyle: "none",
    "& > li": {
      padding: "5px 0px",
      fontSize: "1em"
    }
  },
  profileTabs: {
    marginTop: "4.284rem",
    marginBottom: "50px"
  },
  card: {
    textAlign: "left !important"
  },
  block: {
    color: "inherit",
    padding: "0.9375rem",
    fontWeight: "500",
    fontSize: "12px",
    textTransform: "uppercase",
    borderRadius: "3px",
    textDecoration: "none",
    position: "relative",
    display: "block"
  },
  inlineBlock: {
    display: "inline-block",
    padding: "0px",
    width: "auto"
  },
  list: {
    marginBottom: "0",
    padding: "0",
    marginTop: "0"
  },
  left: {
    float: "left!important",
    display: "block"
  },
  right: {
    padding: "15px 0",
    margin: "0",
    float: "right"
  },
  icon: {
    width: "18px",
    height: "18px",
    top: "3px",
    position: "relative"
  },
  parallax: {
    height: "380px",
    backgroundPosition: "top center"
  },
  headerInfo:{
    height:"80px",
    margin:"20px auto",
    borderRadius:"10px"
  },
  headerLeft:{
    display:"inline-block"
  },
  headerLeftIcon:{
    width:"60px",
    height:"60px",
    margin:"10px",
    borderRadius:"50%",
    display:"inline-block",
    backgroundSize:"100% 100%"
  },
  headerName:{
    display:"inline-block",
    verticalAlign:"top",
    marginTop:"10px",
  },
  headerNameT:{
    color:"red",
    fontSize:"24px",
    marginBottom:"5px"
  },
  headerRight:{
    float:"right",
    lineHeight:"80px",
    marginRight:"15px"
  },
  bodyLeft:{
    margin:"20px 0"
  },
  center:{
    margin:"20px 0"
  },
  centerMoney:{
    height:"210px",
    borderRadius:"22px",
    border:"2px dashed #d5d3cd",
    padding:"20px 5px",
    margin:"20px 0"
  },
  moneyTop:{
    color:"#ffbb10",
    "& svg":{
      fontSize:"21px",
    },
    "& span":{
      fontSize:"31px",
    },
    "& div":{
      color:"#333"
    }
  },
  bodyRight:{
    margin:"20px 0"
  },
  rightTop:{
    height:"260px",
    borderRadius:"22px",
    border:"2px dashed #d5d3cd",
    padding:"2px",
    margin:"20px 0",
    "& textarea":{
      height:"100%",
      width:"100%",
      fontSize:"16px",
      borderRadius:"22px",
      padding:"10px",
      resize:"none",
      backgroundColor:"#fffddd"
    }
  }
  
};

export default profilePageStyle;
