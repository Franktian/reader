import React from 'react';
import {
    View,
    Text,
    TextInput,
    StyleSheet
} from 'react-native';

import TextField from './components/TextField';

class HomeScreen extends React.Component {
    static navigationOptions = {
        title: 'Home',
    };
    render() {
        const { navigate } = this.props.navigation;
        return (
            <View style={styles.container}>
                <TextField
                    label={'User Name'}
                />
                <TextField
                    label={'Password'}
                />
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 10,
    },
    textInput: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1
    }
});

export default HomeScreen;
