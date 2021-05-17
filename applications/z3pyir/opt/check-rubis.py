import sys
sys.path.append("../../")

from z3 import *
from Rigi.axioms import *
from Rigi.checker import *
from Rigi.table import *
from Rigi.tableIns import *
from Rigi.argvbuilder import *

##############################################################################################

winners = Table('winners')
winners.addAttr('winner_id', Table.Type.INT)
winners.addAttr('item_id', Table.Type.INT)
winners.addAttr('bid', Table.Type.REAL)
winners.setPKey('item_id')
winners.build()


buy_now = Table('buy_now')
buy_now.addAttr('id', Table.Type.INT)
buy_now.addAttr('buyer_id', Table.Type.INT)
buy_now.addAttr('item_id', Table.Type.INT)
buy_now.addAttr('qty', Table.Type.INT)
buy_now.addAttr('date', Table.Type.INT)
buy_now.setPKey('id')
buy_now.build()


regions = Table('regions')
regions.addAttr('id', Table.Type.INT)
regions.addAttr('name', Table.Type.STRING)
regions.setPKey('id')
regions.setPKey('name')
regions.build()


comments = Table('comments')
comments.addAttr('id', Table.Type.INT)
comments.addAttr('from_user_id', Table.Type.INT)
comments.addAttr('to_user_id', Table.Type.INT)
comments.addAttr('item_id', Table.Type.INT)
comments.addAttr('rating', Table.Type.INT)
comments.addAttr('date', Table.Type.INT)
comments.addAttr('comment', Table.Type.STRING)
comments.setPKey('id')
comments.build()


bids = Table('bids')
bids.addAttr('id', Table.Type.INT)
bids.addAttr('user_id', Table.Type.INT)
bids.addAttr('item_id', Table.Type.INT)
bids.addAttr('qty', Table.Type.INT)
bids.addAttr('bid', Table.Type.REAL)
bids.addAttr('max_bid', Table.Type.REAL)
bids.addAttr('date', Table.Type.INT)
bids.setPKey('id')
bids.build()


categories = Table('categories')
categories.addAttr('id', Table.Type.INT)
categories.addAttr('name', Table.Type.STRING)
categories.setPKey('id')
categories.build()


items = Table('items')
items.addAttr('id', Table.Type.INT)
items.addAttr('name', Table.Type.STRING)
items.addAttr('description', Table.Type.STRING)
items.addAttr('initial_price', Table.Type.REAL)
items.addAttr('quantity', Table.Type.INT)
items.addAttr('reserve_price', Table.Type.REAL)
items.addAttr('buy_now', Table.Type.REAL)
items.addAttr('nb_of_bids', Table.Type.INT)
items.addAttr('max_bid', Table.Type.REAL)
items.addAttr('start_date', Table.Type.INT)
items.addAttr('end_date', Table.Type.INT)
items.addAttr('seller', Table.Type.INT)
items.addAttr('category', Table.Type.INT)
items.setPKey('id')
items.build()


users = Table('users')
users.addAttr('id', Table.Type.INT)
users.addAttr('firstname', Table.Type.STRING)
users.addAttr('lastname', Table.Type.STRING)
users.addAttr('nickname', Table.Type.STRING)
users.addAttr('password', Table.Type.STRING)
users.addAttr('email', Table.Type.STRING)
users.addAttr('rating', Table.Type.INT)
users.addAttr('balance', Table.Type.REAL)
users.addAttr('creation_date', Table.Type.INT)
users.addAttr('region', Table.Type.INT)
users.setPKey('id')
users.setPKey('nickname')
users.build()


def GenState():
    TABLE_winners = TableInstance(winners)
    TABLE_buy_now = TableInstance(buy_now)
    TABLE_regions = TableInstance(regions)
    TABLE_comments = TableInstance(comments)
    TABLE_bids = TableInstance(bids)
    TABLE_categories = TableInstance(categories)
    TABLE_items = TableInstance(items)
    TABLE_users = TableInstance(users)
    return {'TABLE_winners':TABLE_winners,'TABLE_buy_now':TABLE_buy_now,'TABLE_regions':TABLE_regions,'TABLE_comments':TABLE_comments,'TABLE_bids':TABLE_bids,'TABLE_categories':TABLE_categories,'TABLE_items':TABLE_items,'TABLE_users':TABLE_users}

def GenArgv():
    builder = ArgvBuilder()
    builder.NewOp('RegisterItem_doGet_44')
    builder.AddArgv('reservePrice',ArgvBuilder.Type.REAL)
    builder.AddArgv('quantity',ArgvBuilder.Type.INT)
    builder.AddArgv('endDate',ArgvBuilder.Type.INT)
    builder.AddArgv('initialPrice',ArgvBuilder.Type.REAL)
    builder.AddArgv('nb_of_bids',ArgvBuilder.Type.INT)
    builder.AddArgv('description',ArgvBuilder.Type.STRING)
    builder.AddArgv('userId',ArgvBuilder.Type.INT)
    builder.AddArgv('itemId',ArgvBuilder.Type.INT)
    builder.AddArgv('buyNow',ArgvBuilder.Type.REAL)
    builder.AddArgv('max_bid',ArgvBuilder.Type.REAL)
    builder.AddArgv('name',ArgvBuilder.Type.STRING)
    builder.AddArgv('startDate',ArgvBuilder.Type.INT)
    builder.AddArgv('categoryId',ArgvBuilder.Type.INT)

    builder.NewOp('RegisterUser_doGet_45')
    builder.AddArgv('firstname',ArgvBuilder.Type.STRING)
    builder.AddArgv('password',ArgvBuilder.Type.STRING)
    builder.AddArgv('balance',ArgvBuilder.Type.REAL)
    builder.AddArgv('rate',ArgvBuilder.Type.INT)
    builder.AddArgv('regionId',ArgvBuilder.Type.INT)
    builder.AddArgv('now',ArgvBuilder.Type.INT)
    builder.AddArgv('nickname',ArgvBuilder.Type.STRING)
    builder.AddArgv('region',ArgvBuilder.Type.STRING)
    builder.AddArgv('userId',ArgvBuilder.Type.INT)
    builder.AddArgv('email',ArgvBuilder.Type.STRING)
    builder.AddArgv('lastname',ArgvBuilder.Type.STRING)

    builder.NewOp('StoreBid_doPost_74')
    builder.AddArgv('itemId',ArgvBuilder.Type.INT)
    builder.AddArgv('minBid',ArgvBuilder.Type.REAL)
    builder.AddArgv('maxBid',ArgvBuilder.Type.REAL)
    builder.AddArgv('qty',ArgvBuilder.Type.INT)
    builder.AddArgv('bid',ArgvBuilder.Type.REAL)
    builder.AddArgv('maxQty',ArgvBuilder.Type.INT)
    builder.AddArgv('userId',ArgvBuilder.Type.INT)
    builder.AddArgv('now',ArgvBuilder.Type.INT)
    builder.AddArgv('bidId',ArgvBuilder.Type.INT)
    builder.AddArgv('nbOfBids',ArgvBuilder.Type.INT)

    builder.NewOp('StoreComment_doPost_60')
    builder.AddArgv('toId',ArgvBuilder.Type.INT)
    builder.AddArgv('itemId',ArgvBuilder.Type.INT)
    builder.AddArgv('rating1',ArgvBuilder.Type.INT)
    builder.AddArgv('comment',ArgvBuilder.Type.STRING)
    builder.AddArgv('fromId',ArgvBuilder.Type.INT)
    builder.AddArgv('now',ArgvBuilder.Type.INT)
    builder.AddArgv('commentId',ArgvBuilder.Type.INT)

    builder.NewOp('StoreBuyNow_doPost_77')
    builder.AddArgv('itemId',ArgvBuilder.Type.INT)
    builder.AddArgv('qty',ArgvBuilder.Type.INT)
    builder.AddArgv('maxQty',ArgvBuilder.Type.INT)
    builder.AddArgv('userId',ArgvBuilder.Type.INT)
    builder.AddArgv('orderId',ArgvBuilder.Type.INT)
    builder.AddArgv('now',ArgvBuilder.Type.INT)

    builder.NewOp('CloseAuction_doGet_40')
    builder.AddArgv('itemId',ArgvBuilder.Type.INT)
    builder.AddArgv('bidValue',ArgvBuilder.Type.REAL)
    builder.AddArgv('userId',ArgvBuilder.Type.INT)
    builder.AddArgv('now',ArgvBuilder.Type.INT)

    return builder.Build()

class Op_RegisterItem_doGet_44():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomUniqueArgument('RegisterItem_doGet_44', 'itemId')


    def cond0(self, state, argv):
        return True
    

    def csop0(self, state, argv):
        return True
    

    def sop0(self, state, argv):
        name = argv['RegisterItem_doGet_44']['name']
        description = argv['RegisterItem_doGet_44']['description']
        initialPrice = argv['RegisterItem_doGet_44']['initialPrice']
        quantity = argv['RegisterItem_doGet_44']['quantity']
        reservePrice = argv['RegisterItem_doGet_44']['reservePrice']
        buyNow = argv['RegisterItem_doGet_44']['buyNow']
        nb_of_bids = argv['RegisterItem_doGet_44']['nb_of_bids']
        max_bid = argv['RegisterItem_doGet_44']['max_bid']
        startDate = argv['RegisterItem_doGet_44']['startDate']
        endDate = argv['RegisterItem_doGet_44']['endDate']
        userId = argv['RegisterItem_doGet_44']['userId']
        categoryId = argv['RegisterItem_doGet_44']['categoryId']
        itemId = argv['RegisterItem_doGet_44']['itemId']
        id = itemId
        name = name
        description = description
        initial_price = initialPrice
        quantity = quantity
        reserve_price = reservePrice
        buy_now = buyNow
        nb_of_bids = nb_of_bids
        max_bid = max_bid
        start_date = startDate
        end_date = endDate
        seller = userId
        category = categoryId
        state['TABLE_items'].add({'id' : itemId}, {'name' : name,'description' : description,'initial_price' : initial_price,'quantity' : quantity,'reserve_price' : reserve_price,'buy_now' : buy_now,'nb_of_bids' : nb_of_bids,'max_bid' : max_bid,'start_date' : start_date,'end_date' : end_date,'seller' : seller,'category' : category})
        return state

class Op_RegisterUser_doGet_45():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomUniqueArgument('RegisterUser_doGet_45', 'userId')


    def cond0(self, state, argv):
        region = argv['RegisterUser_doGet_45']['region']
        nickname = argv['RegisterUser_doGet_45']['nickname']
        return And((Not(state['TABLE_regions'].notNil({'name' : region}) == False)),(Not(state['TABLE_users'].notNil({'nickname' : nickname}) == True)))
    

    def csop0(self, state, argv):
        return True
    

    def sop0(self, state, argv):
        firstname = argv['RegisterUser_doGet_45']['firstname']
        lastname = argv['RegisterUser_doGet_45']['lastname']
        nickname = argv['RegisterUser_doGet_45']['nickname']
        password = argv['RegisterUser_doGet_45']['password']
        email = argv['RegisterUser_doGet_45']['email']
        rate = argv['RegisterUser_doGet_45']['rate']
        balance = argv['RegisterUser_doGet_45']['balance']
        now = argv['RegisterUser_doGet_45']['now']
        regionId = argv['RegisterUser_doGet_45']['regionId']
        userId = argv['RegisterUser_doGet_45']['userId']
        id = userId
        firstname = firstname
        lastname = lastname
        nickname = nickname
        password = password
        email = email
        rating = rate
        balance = balance
        creation_date = now
        region = regionId
        state['TABLE_users'].add({'id' : userId}, {'firstname' : firstname,'lastname' : lastname,'nickname' : nickname,'password' : password,'email' : email,'rating' : rating,'balance' : balance,'creation_date' : creation_date,'region' : region})
        return state

class Op_StoreBid_doPost_74():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0),(self.cond1, self.csop1, self.sop1)]
        self.axiom = AxiomUniqueArgument('StoreBid_doPost_74', 'bidId')


    def cond0(self, state, argv):
        qty = argv['StoreBid_doPost_74']['qty']
        maxQty = argv['StoreBid_doPost_74']['maxQty']
        bid = argv['StoreBid_doPost_74']['bid']
        minBid = argv['StoreBid_doPost_74']['minBid']
        maxBid = argv['StoreBid_doPost_74']['maxBid']
        itemId = argv['StoreBid_doPost_74']['itemId']
        return And((Not(qty > maxQty)),(Not(bid < minBid)),(Not(maxBid < minBid)),(Not(maxBid < bid)),((state['TABLE_items'].notNil({'id' : itemId}) == True)),(Not(bid > state['TABLE_items'].get({'id' : itemId}, 'max_bid'))))


    def csop0(self, state, argv):
        return True
    

    def sop0(self, state, argv):
        userId = argv['StoreBid_doPost_74']['userId']
        itemId = argv['StoreBid_doPost_74']['itemId']
        qty = argv['StoreBid_doPost_74']['qty']
        bid = argv['StoreBid_doPost_74']['bid']
        maxBid = argv['StoreBid_doPost_74']['maxBid']
        now = argv['StoreBid_doPost_74']['now']
        bidId = argv['StoreBid_doPost_74']['bidId']
        id = bidId
        user_id = userId
        item_id = itemId
        qty = qty
        bid = bid
        max_bid = maxBid
        date = now
        state['TABLE_bids'].add({'id' : bidId}, {'user_id' : user_id,'item_id' : item_id,'qty' : qty,'bid' : bid,'max_bid' : max_bid,'date' : date})
        nbOfBids = argv['StoreBid_doPost_74']['nbOfBids']
        itemId = argv['StoreBid_doPost_74']['itemId']
        nb_of_bids = state['TABLE_items'].get({'id' : itemId}, 'nb_of_bids')
        nb_of_bids = nb_of_bids + 1
        state['TABLE_items'].update({'id' : itemId}, {'nb_of_bids' : nb_of_bids})
        return state


    def cond1(self, state, argv):
        qty = argv['StoreBid_doPost_74']['qty']
        maxQty = argv['StoreBid_doPost_74']['maxQty']
        bid = argv['StoreBid_doPost_74']['bid']
        minBid = argv['StoreBid_doPost_74']['minBid']
        maxBid = argv['StoreBid_doPost_74']['maxBid']
        bid = argv['StoreBid_doPost_74']['bid']
        itemId = argv['StoreBid_doPost_74']['itemId']
        return And((Not(qty > maxQty)),(Not(bid < minBid)),(Not(maxBid < minBid)),(Not(maxBid < bid)),((state['TABLE_items'].notNil({'id' : itemId}) == True)))
    

    def csop1(self, state, argv):
        bid = argv['StoreBid_doPost_74']['bid']
        itemId = argv['StoreBid_doPost_74']['itemId']
        bid = argv['StoreBid_doPost_74']['bid']
        itemId = argv['StoreBid_doPost_74']['itemId']
        return ((bid > state['TABLE_items'].get({'id' : itemId}, 'max_bid')))
    

    def sop1(self, state, argv):
        userId = argv['StoreBid_doPost_74']['userId']
        itemId = argv['StoreBid_doPost_74']['itemId']
        qty = argv['StoreBid_doPost_74']['qty']
        bid = argv['StoreBid_doPost_74']['bid']
        maxBid = argv['StoreBid_doPost_74']['maxBid']
        now = argv['StoreBid_doPost_74']['now']
        bidId = argv['StoreBid_doPost_74']['bidId']
        id = bidId
        user_id = userId
        item_id = itemId
        qty = qty
        bid = bid
        max_bid = maxBid
        date = now
        state['TABLE_bids'].add({'id' : bidId}, {'user_id' : user_id,'item_id' : item_id,'qty' : qty,'bid' : bid,'max_bid' : max_bid,'date' : date})
        maxBid = argv['StoreBid_doPost_74']['maxBid']
        nbOfBids = argv['StoreBid_doPost_74']['nbOfBids']
        itemId = argv['StoreBid_doPost_74']['itemId']
        max_bid = state['TABLE_items'].get({'id' : itemId}, 'max_bid')
        nb_of_bids = state['TABLE_items'].get({'id' : itemId}, 'nb_of_bids')
        max_bid = maxBid
        nb_of_bids = nb_of_bids + 1
        state['TABLE_items'].update({'id' : itemId}, {'max_bid' : max_bid,'nb_of_bids' : nb_of_bids})
        return state

class Op_StoreComment_doPost_60():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0),(self.cond1, self.csop1, self.sop1)]
        self.axiom = AxiomUniqueArgument('StoreComment_doPost_60', 'commentId')

    def cond0(self, state, argv):
        return True
    

    def csop0(self, state, argv):
        return True
    

    def sop0(self, state, argv):
        fromId = argv['StoreComment_doPost_60']['fromId']
        toId = argv['StoreComment_doPost_60']['toId']
        itemId = argv['StoreComment_doPost_60']['itemId']
        rating1 = argv['StoreComment_doPost_60']['rating1']
        now = argv['StoreComment_doPost_60']['now']
        comment = argv['StoreComment_doPost_60']['comment']
        commentId = argv['StoreComment_doPost_60']['commentId']
        id = commentId
        from_user_id = fromId
        to_user_id = toId
        item_id = itemId
        rating = rating1
        date = now
        comment = comment
        state['TABLE_comments'].add({'id' : commentId}, {'from_user_id' : from_user_id,'to_user_id' : to_user_id,'item_id' : item_id,'rating' : rating,'date' : date,'comment' : comment})
        return state


    def cond1(self, state, argv):
        toId = argv['StoreComment_doPost_60']['toId']
        return And(((state['TABLE_users'].notNil({'id' : toId}) == True)))
    

    def csop1(self, state, argv):
        return True
    

    def sop1(self, state, argv):
        fromId = argv['StoreComment_doPost_60']['fromId']
        toId = argv['StoreComment_doPost_60']['toId']
        itemId = argv['StoreComment_doPost_60']['itemId']
        rating1 = argv['StoreComment_doPost_60']['rating1']
        now = argv['StoreComment_doPost_60']['now']
        comment = argv['StoreComment_doPost_60']['comment']
        commentId = argv['StoreComment_doPost_60']['commentId']
        id = commentId
        from_user_id = fromId
        to_user_id = toId
        item_id = itemId
        rating = rating1
        date = now
        comment = comment
        state['TABLE_comments'].add({'id' : commentId}, {'from_user_id' : from_user_id,'to_user_id' : to_user_id,'item_id' : item_id,'rating' : rating,'date' : date,'comment' : comment})
        rating1 = argv['StoreComment_doPost_60']['rating1']
        toId = argv['StoreComment_doPost_60']['toId']
        rating = state['TABLE_users'].get({'id' : toId}, 'rating')
        rating = rating + rating1
        state['TABLE_users'].update({'id' : toId}, {'rating' : rating})
        return state

class Op_StoreBuyNow_doPost_77():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0),(self.cond1, self.csop1, self.sop1)]
        self.axiom = AxiomUniqueArgument('StoreBuyNow_doPost_77', 'orderId')


    def cond0(self, state, argv):
        qty = argv['StoreBuyNow_doPost_77']['qty']
        maxQty = argv['StoreBuyNow_doPost_77']['maxQty']
        itemId = argv['StoreBuyNow_doPost_77']['itemId']
        return And((Not(qty > maxQty)),(Not(state['TABLE_items'].notNil({'id' : itemId}) == False)),(Not(qty <= 0)),(((state['TABLE_items'].get({'id' : itemId}, 'quantity') - qty) == 0)),(Not(qty == 1)))
    

    def csop0(self, state, argv):
        return True
    

    def sop0(self, state, argv):
        now = argv['StoreBuyNow_doPost_77']['now']
        qty = argv['StoreBuyNow_doPost_77']['qty']
        itemId = argv['StoreBuyNow_doPost_77']['itemId']
        end_date = state['TABLE_items'].get({'id' : itemId}, 'end_date')
        quantity = state['TABLE_items'].get({'id' : itemId}, 'quantity')
        end_date = now
        quantity = quantity - qty
        state['TABLE_items'].update({'id' : itemId}, {'end_date' : end_date,'quantity' : quantity})
        userId = argv['StoreBuyNow_doPost_77']['userId']
        itemId = argv['StoreBuyNow_doPost_77']['itemId']
        qty = argv['StoreBuyNow_doPost_77']['qty']
        now = argv['StoreBuyNow_doPost_77']['now']
        orderId = argv['StoreBuyNow_doPost_77']['orderId']
        id = orderId
        buyer_id = userId
        item_id = itemId
        qty = qty
        date = now
        state['TABLE_buy_now'].add({'id' : orderId}, {'buyer_id' : buyer_id,'item_id' : item_id,'qty' : qty,'date' : date})
        return state


    def cond1(self, state, argv):
        qty = argv['StoreBuyNow_doPost_77']['qty']
        maxQty = argv['StoreBuyNow_doPost_77']['maxQty']
        itemId = argv['StoreBuyNow_doPost_77']['itemId']
        return And((Not(qty > maxQty)),(Not(state['TABLE_items'].notNil({'id' : itemId}) == False)),(Not(qty <= 0)),(Not((state['TABLE_items'].get({'id' : itemId}, 'quantity') - qty) == 0)),(((state['TABLE_items'].get({'id' : itemId}, 'quantity') - qty) > 0)),((qty == 1)))
    

    def csop1(self, state, argv):
        return True
    

    def sop1(self, state, argv):
        qty = argv['StoreBuyNow_doPost_77']['qty']
        itemId = argv['StoreBuyNow_doPost_77']['itemId']
        quantity = state['TABLE_items'].get({'id' : itemId}, 'quantity')
        quantity = quantity - qty
        state['TABLE_items'].update({'id' : itemId}, {'quantity' : quantity})
        userId = argv['StoreBuyNow_doPost_77']['userId']
        itemId = argv['StoreBuyNow_doPost_77']['itemId']
        qty = argv['StoreBuyNow_doPost_77']['qty']
        now = argv['StoreBuyNow_doPost_77']['now']
        orderId = argv['StoreBuyNow_doPost_77']['orderId']
        id = orderId
        buyer_id = userId
        item_id = itemId
        qty = qty
        date = now
        state['TABLE_buy_now'].add({'id' : orderId}, {'buyer_id' : buyer_id,'item_id' : item_id,'qty' : qty,'date' : date})
        return state

class Op_CloseAuction_doGet_40():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()


    def cond0(self, state, argv):
        userId = argv['CloseAuction_doGet_40']['userId']
        itemId = argv['CloseAuction_doGet_40']['itemId']
        now = argv['CloseAuction_doGet_40']['now']
        winner_id = userId
        return And((Not(state['TABLE_items'].notNil({'id' : itemId}) == False)),(state['TABLE_items'].get({'id' : itemId},'end_date') <= now),state['TABLE_bids'].XYRel({'id' : itemId},{'id' : itemId, 'user_id' : winner_id}, 'bid' , RelLessOrEqual()),(Not(state['TABLE_bids'].notNil({'item_id' : itemId}) == False)))
    

    def csop0(self, state, argv):
        return True
    

    def sop0(self, state, argv):
        userId = argv['CloseAuction_doGet_40']['userId']
        bidValue = argv['CloseAuction_doGet_40']['bidValue']
        itemId = argv['CloseAuction_doGet_40']['itemId']
        item_id = itemId
        winner_id = userId
        bid = bidValue
        state['TABLE_winners'].add({'item_id' : itemId}, {'winner_id' : winner_id,'bid' : bid})
        now = argv['CloseAuction_doGet_40']['now']
        itemId = argv['CloseAuction_doGet_40']['itemId']
        end_date = state['TABLE_items'].get({'id' : itemId}, 'end_date')
        end_date = now
        state['TABLE_items'].update({'id' : itemId}, {'end_date' : end_date})
        return state


class rubis():
    def __init__(self):
        self.ops = [Op_RegisterItem_doGet_44(), Op_RegisterUser_doGet_45(), Op_StoreBid_doPost_74(), Op_StoreComment_doPost_60(), Op_StoreBuyNow_doPost_77(), Op_CloseAuction_doGet_40()]
        self.tables = [winners,buy_now,regions,comments,bids,categories,items,users]
        self.state = GenState
        self.argv = GenArgv
        self.axiom = AxiomsAnd(BuildArgvAxiom(self.ops),AxiomCausal('RegisterUser_doGet_45',['userId'],'StoreComment_doPost_60',['toId']),AxiomCausal('RegisterItem_doGet_44',['itemId'],'StoreBid_doPost_74',['itemId']),AxiomCausal('RegisterItem_doGet_44',['itemId'],'StoreBuyNow_doPost_77',['itemId']),AxiomCausal('RegisterItem_doGet_44',['itemId'],'CloseAuction_doGet_40',['itemId']))

def factory():
    cls = globals()["rubis"]
    return cls()

if __name__ == '__main__':
    check_parallel(factory, 8)
