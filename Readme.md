# Language Study



CPP, C #, python syntax and sample coding

'''mermaid

sequenceDiagram
MainContainerForm->>Event : Click Spec Model button
Event->>UserControlSpecModel : Cell Click Event
Event->>UserControlSpecModel : Spec Input
Event->>UserControlSpecModel : Click Save Button
UserControlSpecModel->>UserControlSpecModel : CheckValue
UserControlSpecModel->>UserControlSpecModel : _specModelQuery.SaveInterlock()
UserControlSpecModel->>UserControlSpecModel : BindParameterGrid()
UserControlSpecModel->>Event : Refresh Event

mermaid'''
