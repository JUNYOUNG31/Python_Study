<template>
      <div class="mb-5 col">
        <div class="card border-secondary mb-2" style="width: 19rem; height: 32rem;">
          <img :src="`https://image.tmdb.org/t/p/w500${movieCard.poster_path}`" class="card-img-top mx-auto d-block" style="width: 15rem; height: 21rem;" alt="poster">
          <div class="card-body">
            <h5><b>{{ movieCard.title}}</b></h5>
              <p class="card-text text-center ellipsis">{{ movieCard.overview }}</p>
          </div>
        </div>
      </div>    
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movieCard: Object
  }  
}
</script>

<style>
  .ellipsis {
  width: 15rem;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}
</style>