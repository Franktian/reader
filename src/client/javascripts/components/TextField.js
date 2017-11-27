import React from 'react';
import {
    View,
    Text,
    TextInput,
    StyleSheet
} from 'react-native';

class TextField extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <View style={[styles.container, this.props.containerStyle]}>
                <View style={styles.labelContainer}>
                    <Text>{this.props.label}</Text>
                </View>
                <View style={styles.inputContainer}>
                    <TextInput
                        {...this.props}
                        style={styles.textInput}
                    />
                </View>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {

    },
    labelContainer: {

    },
    inputContainer: {

    },
    textInput: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1
    }
});

export default TextField;
