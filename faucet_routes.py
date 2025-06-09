from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db

faucet_bp = Blueprint('faucet', __name__)

@faucet_bp.route('/claim', methods=['GET', 'POST'])
@login_required
def claim_faucet():
    if request.method == 'POST':
        # Aqui iria a lógica para liberar as moedas para o usuário
        flash('Recompensa reivindicada com sucesso!')
    return render_template('claim_faucet.html')

@faucet_bp.route('/withdraw', methods=['GET', 'POST'])
@login_required
def withdraw():
    if request.method == 'POST':
        # Lógica para processar pedido de saque
        flash('Pedido de saque enviado!')
    return render_template('withdraw.html')
