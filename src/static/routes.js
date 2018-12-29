import React from 'react';
import { Route, Switch } from 'react-router';
import { HomeView, LoginView, ProtectedView, NotFoundView } from './containers';
import requireAuthentication from './utils/requireAuthentication';
import LoginPage from './containers/views/LoginPage/LoginPage';
import SignupPage from './containers/views/SignupPage/SignupPage';
import ProductListPage from './containers/views/ProductListPage/ProductListPage';
import ProductDetails from './containers/views/ProductDetails/ProductDetails';
import Userinfo from './containers/views/UserInfo/UserInfo.jsx';
import UpdatePassword from './containers/views/UpdatePassword/UpdatePassword.jsx';
import ShoppingCart from './containers/views/ShoppingCar/shoppingCart'

export default(
    <Switch>
        {/* <Route exact path="/" component={HomeView} /> */}
        <Route exact path="/" component={ProductListPage} />
        <Route path="/login" component={LoginPage} />
        <Route path="/signup" component={SignupPage} />
        {/* <Route path="/ProductList" component={ProductListPage} /> */}
        <Route path="/ProductDetails/:id" component={ProductDetails} />
        <Route path="/Update" component={UpdatePassword} />
        <Route path="/Userinfo" component={requireAuthentication(Userinfo)} />
        <Route path="/ShoppingCart" component={ShoppingCart} />
        <Route path="/protected" component={requireAuthentication(ProtectedView)} />
        <Route path="*" component={NotFoundView} />
        
    </Switch>

);
