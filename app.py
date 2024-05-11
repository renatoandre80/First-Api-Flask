from flask import Flask,jsonify,request

app=Flask(__name__)

purchase_orders=[
    {
        'id':1,
        'Description':'Item de pedido',
        'itens':[
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


@app.route('/orders/<int:id>')
def get_purchase_order_id(id):
    for po in purchase_orders:
        if po['id']==id:
            return jsonify(po)
    return jsonify(f'{id} não encontrado!!!')

@app.route('/orders',methods=['POST'])
def post_orders():
    request_data=request.get_json()
    purchase_order={
        'id':request_data['id'],
        'Description':request_data['Description'],
        'itens':[]
    }
    purchase_orders.append(purchase_order)

    return jsonify(purchase_order)

@app.route('/orders/<int:id>/itens')
def get_items(id):
    for po in purchase_orders:
        if po['id']==id:
            return jsonify(po['itens'])
        
    return jsonify(f'item não encontrado!!!')

@app.route('/orders/<int:id>/itens',methods=['POST'])
def creat_purchase_orders_itens(id):
    req_data=request.get_json()
    for po in purchase_orders:
        if po['id']==id:
            po['itens'].append({
                'id':req_data['id'],
                'Description':req_data['Description'],
                'price':req_data['price']
            })
            return jsonify(po)
    return jsonify(f'{id} não encontrado!!!')

app.run()