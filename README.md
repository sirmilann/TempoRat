# TempoRat
A Small Rat
To Add Your Own Functions, Go Into TempoModule And Paste This Code ↓
```
def mycustomcommand():
    Your Custom Command Code.
```
after Your Done Adding Your Command, Go To The TempoHost File And Scroll Down Until You See Def run(self):
In The Command Section Add
```
if command[0] == "your command name":
                    TempoModule.Name Of Your Def.
```
