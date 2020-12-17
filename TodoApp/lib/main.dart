import 'package:flutter/material.dart';

void main() {
  runApp(TodoApp());
}

class TodoApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Sample Todo App',
        home: Scaffold(
          appBar: AppBar(
            title: Text('Sample Todo App'),
          ),
          body: LoginState(),
        ));
  }
}

class LoginState extends StatefulWidget {
  _LoginPage createState() => _LoginPage();
}

class _LoginPage extends State<LoginState> {
  @override
  Widget build(BuildContext context) {
    final usernamController = TextEditingController();
    final passwordController = TextEditingController();
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text("Username: "),
            TextField(
              controller: usernamController,
            ),
            Text("Password: "),
            TextField(
              obscureText: true,
              controller: passwordController,
            ),
            FlatButton(
              onPressed: () {
                return showDialog(
                    context: context,
                    builder: (context) {
                      return AlertDialog(
                        content: Text("Username: " + usernamController.text),
                      );
                    });
              },
              child: Text("Login"),
              color: Colors.blue[400],
            )
          ],
        ),
      ),
    );
  }
}
