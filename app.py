from flask import Flask,jsonify

app=Flask(__name__)

purchase_orders=[
    {
        'id':1,
        'Description':'Item de pedido',
        'items':[
            {
                'id':1,
                'Description':'Itens pedido 1',
                'price':'7.90'
            }
        ]
    }
]
@app.route('/')
def get_name():
    return 'Olá Renato André'

@app.route('/orders')
def get_orders():
    return jsonify(purchase_orders)
app.run()