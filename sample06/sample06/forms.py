import colander

class Schema(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    age  = colander.SchemaNode(colander.Integer())
