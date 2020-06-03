<template>
  <div class="modal fade" :id="'movie-'+movie.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <img class="my-3 w-100" :src="movie.backdrop_url" alt="">
          <h3><span class="badge badge-success">{{ movie.user_rating }}</span></h3>
          <p>{{ movie.overview }}</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieListItemModal',
  props: {
    movie: Object
  }
}
</script>

<style>

</style>