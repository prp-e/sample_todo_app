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
          body: Center(
            child: Text("Hello, World!"),
          ),
        ));
  }
}
