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
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text("Username: "),
            TextField(),
            Text("Password: "),
            TextField(),
            FlatButton(onPressed: null, child: Text("Login"))
          ],
        ),
      ),
    );
  }
}
