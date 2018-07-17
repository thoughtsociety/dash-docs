import dash_core_components as dcc
import dash_html_components as html

import styles

layout = [dcc.Markdown('''
  # React for Python developers: a primer

  ## Introduction

  If you're a Dash developer, at some point or another you probably have thought about writing your own set of components for Dash. 
  You might have even taken a peek at some of our source code, or taken the `dash-component-archetype` for a spin. However, if you've 
  never programmed in JavaScript and/or used React before, you might feel slightly confused. This guide hopes to bridge the gap between 
  your knowledge of Python and Dash and the languages and frameworks we use to create awesome Dash components!

  #### JavaScript
  JavaScript is the language of the web - all modern browsers can run it, and most modern web pages use it to make their pages interactive.
  It is the de-facto standard of front end development, and has come a long way since it's inception. Today, modern JavaScript features
  a rich set of features, designed to create a development experience perfectly suited for the web. 

  #### React
  React is JavaScript library for building user interfaces, written and maintained by Facebook. It has been very popular over the last few
  years, mainly because it brings the power of reactive, declarative programming to the world of front end development. 
  What this means is that it brings power to those programming complex applications on the web, giving them the ability to write highly 
  interactive web pages in a single language.

  It is important to realise that React is just JavaScript. React is not a language on it's own, nor is it any sort of domain-specific framework
  that takes years to master. It has a relatively small API to learn, with just a few functions and paradigms to get your head around before
  you too can use it to write applications for the web. That being said, all unfamiliar technology will have a learning curve, but with practice
  and patience you will master it!

  Dash uses React under the hood to render the user interface you see when you load a web page created with Dash. Because React allows you to write
  your user interface in encapsulated components that manage their own state, it is easy to split up parts of code for Dash too - at the end of this
  tutorial, you will see that Dash components and React components map 1 to 1! For now, it is important to know that Dash components are 
  mostly just simple wrappers around existing React components. This means the entire React ecosystem is potentially usable in a Dash application!

  ## Installing everything you need
  Let's start by setting up our JavaScript development environment. We will use Node.js, NPM, and `create-react-app` to write our first React
  application. Node.js is a JavaScript runtime, which allows you to run JavaScript code outside of the browser. Just like you would run 
  `python my-code.py` to run Python code in a terminal, you'd run `node my-code.js` to run JavaScript code in a terminal. 
  Node comes in very handy when developing, even when you intend to run the code in the browser.
  With Node we can take advantage of the extensive tooling, provided by NPM, which stands for Node Package Manager (Node's version of `pip`), 
  that is available today when writing in JavaScript. 
  One of those tools is `create-react-app`, built by the core team behind React. This tool allows you to very easily set up a new React project. 
  It handles basically everything for you, from setting up tools that watch and reload your code
  to running a local server so you can see what your app looks like. It even sets up a system called `webpack`, which bundles all your code and assets
  together and - you guessed it - packs it up for the web.

  - To install Node.js, go to [the Node.js website](https://nodejs.org/en/) to download the latest (stable) version. 
  - Node.js will automatically install the Node Package Manager `npm` on your machine
  - Verify that node is installed by running: `node -v`
  - Verify that npm is installed by running: `npm -v`

  Now that we have Node.js up and running, we'll go ahead and initialize a new project using `create-react-app` by running:
  - `npm init react-app my-app`

  This sets up everything you need for a React application! It will give you some instructions on how to start it up after it's done
  installing, most likely it will tell you to run `yarn start`. Yarn is another JavaScript package manager, which you can also use
  instead of NPM. It's up to you - either `npm start` or `yarn start` will work!

  ## Quick intro to React

  Now, let's go ahead and see what the code for our new React application looks like. Open up your favourite code editor, and open the `src/App.js` file.
  This is your first React component! In React, most of the code you write will reside in some sort of a component. This is the top-level component, apptly named `App`, which job it is to basically be the entry point of the app. Here you will render all other components that you want to be displayed. Try changing the 
  "Welcome to React" text to "Welcome to Dash", and save it. Now, go back to the browser, and notice how it hot-reloads the page!

  #### JSX
  You probably already noticed that the text you changed was wrapped in a `<h1>` tag. It looks like HTML, but slightly different! What gives? This is
  what is called JSX. A language developed by the React team to have easy, inline, HTML markup in your JavaScript components! Don't let the word 'language' scare
  you - it is mostly exactly the same as regular HTML. The main difference lies in the naming of attributes - `class` (for appending a CSS class to an HTML tag) is
  named `className` here, as to avoid confusion with the actual `class` keyword in JavaScript (yes, JavaScript has classes, just like in Python!).


  #### Virtual DOM
  If we look at the `App` component again, we see that it is `export`ed at the bottom, and if you open up the `src/index.js` file you can see that it's imported there, so it can be used in a call to `ReactDOM.render()`. 
  This `ReactDOM.render()` method is only called here, and only once. All it does is render our `App` component in a `div` element with the `id` of `root`. React handles all of the rendering of 
  components internally, using a very smart system called the Virtual DOM. It does this so it can update DOM nodes internally in the most efficient and fast way, meaning we
  only have to concentrate on declaring how we want things to look like, and how we want things to behave! 

  #### Classes
  Now, as a Python developer, classes are probably nothing new to you. In the JavaScript community, however, classes are a relatively new addition. They've become available to us
  in `ES6`, which stands for EcmaScript 6 - an updated version of JavaScript. React greatly benefits from this enhanced versions of JavaScript, so they decided
  to set us up with a transpiler called Babel. Babel is nothing more than a tool that converts (or transpiles) your ES6 (or ES7 and ES8) code into JavaScript
  all browsers can understand (even older ones like Internet Explorer!). This allows us to write modern JavaScript - which includes classes - whilest not having to worry (too much) about browser support. Babel comes included with `create-react-app`.

  We see here in our `App` component that it is defined as a `class` which `extends` from the `Component` class of React. This provides some methods to us, for example the `render()` method we're using here. `render()` is the method that is called by the *component that is rendering it*. In our case, `render()` is called
  by the `ReactDOM.render()` call in `index.js`. Notice how the `<App />` is called in the `ReactDOM.render()` method: our `App` component is used as a JSX tag!

  #### Other methods on React.Component
  Other methods provided by React are mostly related to component state management. We've got lifecycle hooks like `shouldComponentUpdate` and `componentDidMount` which allow you to better specify when and how a component should update. For these methods, please refer to the [React documentation](https://reactjs.org/docs/state-and-lifecycle.html)

  ## Our very own React component
  Now, let's create our very own component. Create a file in `src`, and let's name it `TextInput.js`. In the `TextInput.js` file, let's first import React 
  and React.Component (the { Component } syntax is a shorthand) the same way as in `App.js` by writing `import React, { Component } from 'react'`.

  Next, let's define our component by writing it as a class, which extends React.Component. 

  ```
  import React, { Component } from 'react';

  class TextInput extends Component {
    // here we'll define everything we need our TextInput component to have
  }
  ```

  Next, we'll write a `constructor` method on our component. A class constructor in Python is usually defined as `def __init__()` on a class, but in JavaScript
  we use the `constructor()` syntax. In the constructor, we call the `super()` method on our component's props (more on props later), and set some `state`.
  It will look like this: 

  ```
  import React, { Component } from 'react';

  class TextInput extends Component {
    constructor(props) {
      super(props);
      this.state = {
        value: 'default'
      }
    }
  }
  ```

  `props` are a component's properties. They are passed down from a component's parent, and are available as the `props` attribute. Calling `super()` on `props` in the constructor, makes our props available in the component as `this.props`. The `this` keyword in JavaScript is Python's `self`. We'll show you how to pass down
  `props` a bit later on.

  We're also defining `this.state` here, which is an `object`. `object`'s in JavaScript are a lot like `dict`'s in Python. They are specified in a notation
  called `JSON`, which stands for JavaScript Object Notation. We're setting a `key` on our `state` object, called `value`, to be a string, 'default'.

  Next, let's define our `render()` method, because all components should render something! Every `render()` method should `return` something, in our case, we'll return a HTML/JSX tag, `<input/>`. 
  We'll also go ahead and `export` our component, as the `default`. This means whenever we're trying to `import` something from this file, and we don't specify a name, we'll get the `default` export.

  ```
  import React, { Component } from 'react';

  class TextInput extends Component {
    constructor(props) {
      super(props);
      this.state = {
        value: 'default'
      }
    }
    render() {
      return <input />
    }
  }
  
  export default TextInput;
  ```

  Now, let's `import` that component and use it in our `App` component! Add the `import TextInput from './TextInput';` line to `App.js`, and somewhere
  in the return of our `render()` method, use our newly created `<TextInput />` component.

  Tada!

  We've got a text input. 
  
  However, this input doesn't really do much - it's not connected to anything, nor does it save what you type in. Let's change our `render()` method of `TextInput` to
  set the HTML `value` attribute on our `<input />` tag, so it looks like this: `<input value='dash' />`. Save it, and we should now see that the value of our <input> tag
  is set to 'dash'! We can also change our value to be that which is defined in our `state` object, so `<input value={this.state.value} />`. The `{}` syntax in JSX means 
  that we want to write inline JavaScript in our JSX/HTML, so our `this.state.value` statement can be computed. Great! Now our input says 'default'! Unfortunately, our input
  is still not very useful, because we can't change our input's value, try as we might.  

  We'll need to write some sort of event handler for this. Luckily, we can handle this all in React! We can define methods on our component's class, and use those in our `<input/>` tag.

  ```
  import React, { Component } from 'react';

  class TextInput extends Component {
    constructor(props) {
      super(props);
      this.state = {
        value: 'default'
      }
    }
    handleInputChange = (e) => {
      // get the value from the DOM node
      const newValue = e.target.value;
      // update the state!
      this.setState({
        value: newValue
      })
    }
    render() {
      return <input value={this.state.value} onChange={this.handleInputChange}/>
    }
  }
  
  export default TextInput;
  ```
  Here we wrote a method which we set on our HTML's input `onchange` attribute (written as `onChange` in JSX), which will fire
  every time an `onchange` event happens on our input. This method has a parameter we named `e` for event, on which certain attributes are
  set: `target.value` is what we need. This is how the HTML DOM works - for more information check out [these docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/text).

  You might also wonder what the `const` keyword means. In JavaScript, we have a variety of keywords used to define *in which scope a variable lives*. I won't go into the details too deeply, but
  the basic idea is that we have a `const` keyword to make a variable constant, i.e. you cannot modify it after creation. You can use the `let` keyword, which is not constant, but is bound to
  the scope of the enclosing method, or the `var` keyword, which is also not constant, but, it's scope is broader. In React, it's best to just use `let` for normal variables, and `const` if 
  you want the variable to be unchangable after definition.

  Next, we use a method called `setState()` on our class, provided by `React.Component`. This method will handle updates to our `state` object. Because of how JavaScript works, setting `state`
  directly will result in the *component not updating, thus not firing render() again, so we are not able to see our changes!*. This has to do with the updating of the internal state array - because
  it is not a new object (as happens in `setState()`, it is not recognized as new) [here's a good article on the subject.](https://daveceddia.com/why-not-modify-react-state-directly/)

  See how this now allows you to type in our input component? We can also display our state, by writing our `render()` method something like:

  ```
  render() {
    return <div>
      <input value={this.state.value} onChange={this.handleInputChange} />
      <p>{this.state.value}</p>
    </div>
  }
  ``` 

  Notice that we're not allowed to return multiple elements from `render()`, but an element with children is totally fine.

  We can also pass along properties to our components, via the before mentioned `props`. This works the same as assigning attributes on a component, as we'll demonstrate by adding a `label` prop to our `TextInput` component!
  Let's edit our call to `<TextInput />` to say `<TextInput label='dash-input' />`. This means we now have a `prop` called `label` available on our `TextInput` component! 
  In `TextInput`, we can reference this via `this.props`. Let's extend our `render()` method further so it renders our `label` prop:

  ```
  render() {
    return <div>
      <label>{this.props.label}</label>
      <input value={this.state.value} onChange={this.handleInputChange} />
      <p>{this.state.value}</p>
    </div>
  }
  ``` 

  Props always flow down, but you can set a method as a prop too, so that a child can call a method of a parent. For more information, please refer to the [React docs](https://reactjs.org/docs/components-and-props.html)

  These are just the basics of React, if you want to know more, the [React docs](https://reactjs.org/docs) are a great place to start!

  ## Using your React components in Dash

  We can use most, if not all, components build in React in Dash! Dash uses React under the hood, specifically in the `dash-renderer`. The `dash-renderer` is basically just a React app, that renders the
  layout defined in your Dash app as `app.layout`! It is also resposible for assigning the callbacks you write in Dash to the proper components, and keeping everything up-to-date. The `App` component
  we have been working with so far can simply be thought of as `dash-renderer`!

  There are, of course, some steps you must take for your component to work nicely with Dash. The `props` you want to be available in Dash, should be specified as `propTypes` on the React component, so that the
  Dash Component Archetype (note: this here will need some clarification) can read them and convert them to React. In our example, we can easily do this by changing our code like so:
  ```
  // other imports
  import PropTypes from 'prop-types';

  class TextInput extends Component {
    // class definition here
  }

  TextInput.propTypes = {
    /** 
    * This comment will also get parsed by Dash, 
    * so that it is available in help(component.TextInput)
    **/
    label: PropTypes.string
  }
  ```

  Because we specified what props our component will recieve, Dash is able to read this and make those props available in Dash!
  This means we could use our component in Dash:
  ```
  app.layout = html.Div[
    ourCustomComponent.TextInput(label='great!')
  ]
  ```

  We also have a special prop available called `setProps`. This is Dash's way of keeping state *within Dash* (so not internally in our React component). You can think of it
  as `setState()`, but for Dash. In your React component, you can thus call `this.props.setProps` (if it is set) *instead* of `this.setState()`, and the state will be handled
  in Dash instead of in React! We can re-write our `TextInput` component as follows:
  ```
  import React, { Component } from 'react';
  import PropTypes from 'prop-types';

  class TextInput extends Component {
    constructor(props) {
      super(props);
    }
    handleInputChange = (e) => {
      // get the value from the DOM node
      const newValue = e.target.value;

      // update the props!
      this.props.setProps({
        value: newValue
      })
    }
    render() {
      return <input value={this.props.value} onChange={this.handleInputChange}/>
    }
  }

  TextInput.propTypes = {
    /** 
    * This comment will also get parsed by Dash, 
    * so that it is available in help(component.TextInput)
    **/
    label: PropTypes.string,

    /** 
    * The value of the text input (coming from Dash)
    **/
    value: PropTypes.string,

    /** 
    * Dash-provided callback for keeping state
    **/
    setProps: PropTypes.function
  }
  
  export default TextInput;
```

Note that if you run this example above in our `create-react-app`, `setProps` is not defined - because we're not running this from Dash yet - Dash will make sure the `setProps` prop is
defined! You can provide a `setProps` method yourself ofcourse, because like we said before, `App` is basically like `dash-renderer`:

```
import React, { Component } from "react";
import TextInput from "./TextInput";
import logo from "./logo.svg";
import "./App.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: "App/dash-renderer provided props!"
    };
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <TextInput
          label="dash-input"
          value={this.state.value}
          setProps={(newProps) => {
            this.setState(newProps);
          }}
        />
      </div>
    );
  }
}

export default App;
```

We set `setProps` here to be a new function (an arrow function, read about them [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)) that calls
`setState()` with the new props provided by `setProps`. We also set the `value` of our `TextInput` component to be equal to `this.state.value`, and voila! That is the basics of how Dash and `dash-renderer` work
together.

''')]