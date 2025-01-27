# Markdown Syntaxes

> [!WARNING]
> There are Markdown specific and GitHub specific syntaxes!

> [!NOTE]
> Many thanks to <a href="https://markdown-it.github.io/">markdown-it</a>, 
while it provided the foundation of this documentation.

## Table of contents

-   [Headings](#heading-h1)
-   [Horizontal Rules](#horizontal-rules)
-   [Typographic replacements](#typographic-replacements)
-   [Emphasis](#emphasis)
-   [Blockquotes](#blockquotes)
-   [Lists](#lists)
-   [Code](#code)
-   [Tables](#tables)
-   [Collapsible section](#collapsible-section)
-   [Links](#links)
-   [Bookmarks](#bookmarks)
-   [Images](#images)
-   [Plugins](#plugins)
-   [Arrows](#Arrows)
-   [Emojies](#emojies)
-   [Subscript / Superscript](#subscript--superscript)
-   [\<ins>](#ins)
-   [\<mark>](#mark)
-   [Definition lists](#definition-lists)
-   [Abbreviations](#abbreviations)
-   [Custom containers](#custom-containers)
-   [Alerts](#alerts)
-   [Footnotes](#footnotes)

# Heading h1

## Heading h2

### Heading h3

#### Heading h4

##### Heading h5

###### Heading h6

<details>
    <summary>Raw view</summary>
    
```
# Heading h1

## Heading h2

### Heading h3

#### Heading h4

##### Heading h5

###### Heading h6
```
</details>

## Horizontal Rules

---

***

---

<details>
    <summary>Raw view</summary>
    
```
---

***

---
```
</details>

## Typographic replacements

Enable typographer option to see result.

(c) (C) (r) (R) (tm) (TM) (p) (P) +-

test.. test... test..... test?..... test!....

!!!!!! ???? ,, -- ---

"Smartypants, double quotes" and 'single quotes'

## Emphasis

**This is bold text**

<b>This is bold text</b>

<strong>This is bold text</strong>

*This is italic text*

_This is italic text_

<i>This is italic text</i>

~~Strikethrough~~

<details>
    <summary>Raw view</summary>
    
```
**This is bold text**

<b>This is bold text</b>

<strong>This is bold text</strong>

*This is italic text*

_This is italic text_

<i>This is italic text</i>

~~Strikethrough~~
```
</details>

## Blockquotes

> Blockquotes can also be nested...
>
> > ...by using additional greater-than signs right next to each other...
> >
> > > ...or with spaces between arrows.

<details>
    <summary>Raw view</summary>
    
```
> Blockquotes can also be nested...
>
> > ...by using additional greater-than signs right next to each other...
> >
> > > ...or with spaces between arrows.
```
</details>

## Lists

Unordered

-   Create a list by starting a line with `+`, `-`, or `*`
-   Sub-lists are made by indenting 2 spaces:
    -   Marker character change forces new list start:
        -   Ac tristique libero volutpat at
        *   Facilisis in pretium nisl aliquet
        -   Nulla volutpat aliquam velit
-   Very easy!

<details>
    <summary>Raw view</summary>
    
```
-   Create a list by starting a line with `+`, `-`, or `*`
-   Sub-lists are made by indenting 2 spaces:
    -   Marker character change forces new list start:
        -   Ac tristique libero volutpat at
        *   Facilisis in pretium nisl aliquet
        -   Nulla volutpat aliquam velit
-   Very easy!
```
</details>

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa

4. You can use sequential numbers...
5. ...or keep all the numbers as `1.`

<details>
    <summary>Raw view</summary>
    
```
1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa

4. You can use sequential numbers...
5. ...or keep all the numbers as `1.`
```
</details>

Start numbering with offset:

57. foo
1. bar

<details>
    <summary>Raw view</summary>
    
```
57. foo
1. bar
```
</details>

Checkboxes

-   [ ] not completed
-   [x] completed

<details>
    <summary>Raw view</summary>
    
```
-   [ ] not completed
-   [x] completed
```
</details>

## Code

Inline `code`

Indented code

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code

Block code "fences"

```
Sample text here...
```

Syntax highlighting

```js
var foo = function (bar) {
    return bar++;
};

console.log(foo(5));
```

<details>
    <summary>Raw view</summary>
    
```
Inline `code`

Indented code

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code

Block code "fences"

    ```
    Sample text here...
    ```

Syntax highlighting

    ```js
    var foo = function (bar) {
        return bar++;
    };
    
    console.log(foo(5));
    ```
```
</details>

## Tables

| Option | Description                                                               |
| ------ | ------------------------------------------------------------------------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default.    |
| ext    | extension to be used for dest files.                                      |

<details>
    <summary>Raw view</summary>
    
```
| Option | Description                                                               |
| ------ | ------------------------------------------------------------------------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default.    |
| ext    | extension to be used for dest files.                                      |
```
</details>

Column alignment

| Left   |                                  Center                                   | Right |
| :----- | :-----------------------------------------------------------------------: | ----: |
| data   | path to data files to supply the data that will be passed into templates. |   100 |
| engine |  engine to be used for processing templates. Handlebars is the default.   |   120 |
| ext    |                   extension to be used for dest files.                    |   123 |

<details>
    <summary>Raw view</summary>
    
```
| Left   |                                  Center                                   | Right |
| :----- | :-----------------------------------------------------------------------: | ----: |
| data   | path to data files to supply the data that will be passed into templates. |   100 |
| engine |  engine to be used for processing templates. Handlebars is the default.   |   120 |
| ext    |                   extension to be used for dest files.                    |   123 |
```
</details>

Nested tables

<table><tr><th>First Table</th><th>Second Table</th><th>Last Table</th></tr><tr><td>

| Field_A  |
| -------- |
| value_11 |
| value_12 |
| value_13 |

</td><td>

| Field_B  | Field_C  | Field_D  |
| -------- | -------- | -------- |
| value_21 | Value_31 | Value_41 |
| value_22 | Value_32 | Value_42 |

</td><td>

| Field_E  | Field_F  |
| -------- | -------- |
| value_51 | Value_61 |
| value_52 | Value_62 |
| value_53 | Value_63 |

</td></tr></table>

<details>
    <summary>Raw view</summary>

```
<table>
    <tr>
        <th>First Table</th>
        <th>Second Table</th>
        <th>Last Table</th>
    </tr>
    <tr>
        <td>
            | Field_A  |
            | -------- |
            | value_11 |
            | value_12 |
            | value_13 |
        </td>
        <td>
            | Field_B  | Field_C  | Field_D  |
            | -------- | -------- | -------- |
            | value_21 | Value_31 | Value_41 |
            | value_22 | Value_32 | Value_42 |
        </td>
        <td>
            | Field_E  | Field_F  |
            | -------- | -------- |
            | value_51 | Value_61 |
            | value_52 | Value_62 |
            | value_53 | Value_63 |
        </td>
    </tr>
</table>
```
</details>

## Collapsible section

<details>
  <summary>Click me</summary>
  
  ### Heading
  1. Foo
  2. Bar
     * Baz
     * Qux

  ### Some Javascript
  ```js
  function logSomething(something) {
    console.log('Something', something);
  }
  ```
</details>

<details>
    <summary>Raw view</summary>
    
```
<details>
    <summary>Click me</summary>
        print("Hello World!")
</details>
```
</details>

## Links

[link text](http://dev.nodeca.com)

[link with title](http://nodeca.github.io/pica/demo/ "title text!")

<details>
    <summary>Raw view</summary>
    
```
[link text](http://dev.nodeca.com)

[link with title](http://nodeca.github.io/pica/demo/ "title text!")
```
</details>

Autoconverted link https://github.com/nodeca/pica (enable linkify to see)

## Bookmarks

go to [Lists](#lists)

go to [Code](#code)

go to [Tables](#tables)

<details>
    <summary>Raw view</summary>
    
```
go to [Lists](#lists)

go to [Code](#code)

go to [Tables](#tables)
```
</details>

## Images

![Minion](https://octodex.github.com/images/minion.png)

Labeled image:

![Stormtroopocat](https://octodex.github.com/images/stormtroopocat.jpg "The Stormtroopocat")

Like links, Images also have a footnote style syntax

![Alt text][id]

With a reference later in the document defining the URL location:

[id]: https://octodex.github.com/images/dojocat.jpg "The Dojocat"

The following image is sized, centered and linked:

<p align="center">
    <a href="https://octodex.github.com/" target="_blank">
        <img
            src="https://octodex.github.com/images/boxertocat_octodex.jpg"
            alt="DIKW-pyramid"
            width="300"
        />
    </a>
</p>


## Plugins

The killer feature of `markdown-it` is very effective support of
[syntax plugins](https://www.npmjs.org/browse/keyword/markdown-it-plugin).

### Arrows

| Arrow  | Direction | Code     |
| ------ | --------- | -------- |
| &uarr; | Up        | `&uarr;` |
| &darr; | Down      | `&darr;` |
| &larr; | Left      | `&larr;` |
| &rarr; | Right     | `&rarr;` |
| &harr; | Double    | `&harr;` |

### [Emojies](https://github.com/markdown-it/markdown-it-emoji)

> Classic markup: :wink: :cry: :laughing: :yum:
>
> Shortcuts (emoticons): :-) :-( 8-) ;)

see [how to change output](https://github.com/markdown-it/markdown-it-emoji#change-output) with twemoji.

### [Subscript](https://github.com/markdown-it/markdown-it-sub) / [Superscript](https://github.com/markdown-it/markdown-it-sup)

-   19^th^
-   H~2~O

### [\<ins>](https://github.com/markdown-it/markdown-it-ins)

++Inserted text++

### [\<mark>](https://github.com/markdown-it/markdown-it-mark)

==Marked text==

### [Definition lists](https://github.com/markdown-it/markdown-it-deflist)

Term 1

: Definition 1
with lazy continuation.

Term 2 with _inline markup_

: Definition 2

        { some code, part of Definition 2 }

    Third paragraph of definition 2.

_Compact style:_

Term 1
~ Definition 1

Term 2
~ Definition 2a
~ Definition 2b

### [Abbreviations](https://github.com/markdown-it/markdown-it-abbr)

This is HTML abbreviation example.

It converts "HTML", but keep intact partial entries like "xxxHTMLyyy" and so on.

\*[HTML]: Hyper Text Markup Language

### [Custom containers](https://github.com/markdown-it/markdown-it-container)

::: warning
_here be dragons_
:::

### Alerts

> [!NOTE]
> Useful information that users should know, even when skimming content.

<details>
    <summary>Raw view</summary>

    > [!NOTE]
    > Useful information that users should know, even when skimming content.

</details>

> [!TIP]
> Helpful advice for doing things better or more easily.

<details>
    <summary>Raw view</summary>

    > [!TIP]
    > Helpful advice for doing things better or more easily.

</details>

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

<details>
    <summary>Raw view</summary>

    > [!IMPORTANT]
    > Key information users need to know to achieve their goal.

</details>

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

<details>
    <summary>Raw view</summary>

    > [!WARNING]
    > Urgent info that needs immediate user attention to avoid problems.

</details>

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

<details>
    <summary>Raw view</summary>

    > [!CAUTION]
    > Advises about risks or negative outcomes of certain actions.

</details>

### [Footnotes](https://github.com/markdown-it/markdown-it-footnote)

Footnote 1 link[^first].

Footnote 2 link[^second].

Inline footnote^[Text of inline footnote] definition.

Duplicated footnote reference[^second].

[^first]: Footnote **can have markup**

    and multiple paragraphs.

[^second]: Footnote text.
