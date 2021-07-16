<template>
    <div class="pt-5">
        <div v-if="departamentos && departamentos.length">
            <div class="card mb-3" v-for="departamento of departamentos" v-bind:key="departamento.id">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <div class="card-body">
                            <p class="card-title"> <b>Nombre:</b> {{ departamento.nombre_propietario }}</p>
                            <p class="card-text"><b>Costo:</b> {{ departamento.costo }}</p>
                            <br>
                            <router-link :to="{name: 'edit_departamento', params: { id: departamento.id }}" class="btn btn-sm btn-primary">Editar</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteDepartamento(departamento)">Eliminar</button>
                        </div>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <p class="card-text"><b>Número de cuartos:</b> {{ departamento.num_cuartos }}</p>
                            <p class="card-text"><b>Edificio:</b> {{ departamento.edificio_str }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p  v-if="departamentos.length == 0"> Sin Departamentos</p>
    </div>
</template>
<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamentos: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        deleteDepartamento: function(departamento) {
            if (confirm('Eliminar el departamento de: ' + departamento.nombre_propietario)) {
                axios.delete(departamento.url)
                    .then( response => {
                        this.all();
                    });
            }
        },
        all: function () {
            axios.get('http://127.0.0.1:8090/api/departamentos/')
                .then( response => {
                    this.departamentos = response.data.results
                });
        }
    },
}
</script>
