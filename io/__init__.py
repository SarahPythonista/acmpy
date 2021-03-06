""" The acm.io package

This package includes two classes that simplify I/O operations.

The first is <a href="IOConsole.html"><code>IOConsole</code></a>, which provides
a traditional interactive console.

The second is <a href="IODialog.html"><code>IODialog</code></a>, which
provides a dialog-based input mechanism that is compatible with the console
design.

Each of these classes implements the <a href="IOModel.html"><code>IOModel</code></a>
interface, which unifies the two input models.
"""
__all__ = [
    'console',
    'dialog',
    'model',
]
