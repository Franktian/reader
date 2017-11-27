import React from 'react';
import {
    View,
    Text,
    Button,
    TextInput,
    StyleSheet
} from 'react-native';

import TextField from './components/TextField';
import {
    login,
    register
} from './api/auth';

class HomeScreen extends React.Component {
    static navigationOptions = {
        title: 'Home',
    };

    constructor(props) {
        super(props);

        this.state = {
            username: '',
            password: ''
        };

        this.onLoginPress = this.onLoginPress.bind(this);
        this.onRegisterPress = this.onRegisterPress.bind(this);
    }

    render() {
        const { navigate } = this.props.navigation;
        return (
            <View style={styles.container}>
                <TextField
                    label={'User Name'}
                    onChangeText={username => this.setState({username})}
                />
                <TextField
                    label={'Password'}
                    onChangeText={password => this.setState({password})}
                />
                <Button
                    onPress={this.onLoginPress}
                    title="Login"
                />
                <Button
                    onPress={this.onRegisterPress}
                    title="Register"
                />
            </View>
        );
    }

    onLoginPress() {
        login(this.state.username, this.state.password).then(json => {
            console.log('login', json);
        });
    }

    onRegisterPress() {
        register(this.state.username, this.state.password).then(json => {
            console.log('register', json);
        });
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 10,
        backgroundColor: 'white'
    },
    textInput: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1
    }
});

export default HomeScreen;
